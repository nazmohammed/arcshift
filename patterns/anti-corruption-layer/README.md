# Anti-Corruption Layer Pattern

## Intent

Isolate the modern system from legacy data models and APIs by placing a translation layer at the boundary, preventing legacy concepts from leaking into the new architecture.

## Problem

When a modern service needs to call a legacy system, directly consuming legacy APIs or data models couples the new code to outdated schemas, naming conventions, and business logic quirks. Over time this corruption spreads throughout the modern codebase.

## Solution

Create a dedicated translation layer that converts between legacy and modern domain models at the integration boundary.

```
┌────────────┐     ┌───────────────────┐     ┌────────────┐
│  Modern    │────▶│ Anti-Corruption   │────▶│  Legacy    │
│  Service   │◀────│     Layer (ACL)   │◀────│  System    │
└────────────┘     └───────────────────┘     └────────────┘
                   │ • Model mapping   │
                   │ • Protocol adapt   │
                   │ • Error translate  │
                   └───────────────────┘
```

## When to Use

- Modern service must consume legacy APIs during migration
- Legacy data model uses different naming, types, or structures
- You want to isolate legacy changes from modern code

## When NOT to Use

- Legacy system is being decommissioned immediately
- The integration is temporary and trivial (single field mapping)
- Both systems share the same bounded context and model

## Implementation

### 1. Define Modern Domain Models

```csharp
// Modern domain model — clean, typed, well-named
public record Order(
    Guid Id,
    string CustomerId,
    List<OrderLine> Lines,
    OrderStatus Status,
    DateTimeOffset CreatedAt);
```

### 2. Create the ACL Adapter

```csharp
public class LegacyOrderAdapter : IOrderRepository
{
    private readonly LegacyApiClient _legacy;

    public async Task<Order> GetOrderAsync(Guid id)
    {
        // Call legacy system
        var legacyOrder = await _legacy.GetOrd(id.ToString());

        // Translate to modern model
        return new Order(
            Id: Guid.Parse(legacyOrder.ORD_ID),
            CustomerId: legacyOrder.CUST_NO.ToString(),
            Lines: legacyOrder.ITEMS.Select(MapLineItem).ToList(),
            Status: MapStatus(legacyOrder.STS_CD),
            CreatedAt: DateTimeOffset.Parse(legacyOrder.CRT_DT));
    }

    private static OrderStatus MapStatus(string code) => code switch
    {
        "A" => OrderStatus.Active,
        "C" => OrderStatus.Completed,
        "X" => OrderStatus.Cancelled,
        _ => OrderStatus.Unknown
    };
}
```

### 3. Register via Dependency Injection

```csharp
// During migration: use ACL adapter
services.AddScoped<IOrderRepository, LegacyOrderAdapter>();

// After migration: swap to direct implementation
services.AddScoped<IOrderRepository, OrderRepository>();
```

## Key Principles

- **One ACL per bounded context boundary** — Don't create a single global translator
- **Own the interface** — The modern side defines the contract; the ACL adapts
- **Translate errors too** — Map legacy error codes to modern exceptions
- **Temporary by design** — Remove the ACL once the legacy system is decommissioned

## Related Patterns

- [Strangler Fig](../strangler-fig/README.md) — Gradually routes traffic from legacy to modern
- [Database per Service](../database-per-service/README.md) — Data isolation that ACL supports
