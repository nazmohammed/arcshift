# Branch by Abstraction Pattern

## Intent

Replace a legacy implementation with a modern one by introducing an abstraction layer within the codebase, allowing both implementations to coexist and the switch to happen without long-lived feature branches.

## Problem

Long-lived feature branches for migration work cause merge conflicts, drift from the main codebase, and delay feedback. You need a way to work on the replacement incrementally on the main branch without breaking existing functionality.

## Solution

1. Create an interface (abstraction) for the component being replaced
2. Make the legacy code implement the interface
3. Build the new implementation behind the same interface
4. Switch between implementations using configuration or feature flags
5. Remove the legacy implementation once the new one is verified

```
                    ┌──────────────────┐
                    │   IOrderRepo     │ ◁── Abstraction
                    │  + GetOrders()   │
                    │  + SaveOrder()   │
                    └────────┬─────────┘
                             │
                ┌────────────┼────────────┐
                │                         │
    ┌───────────▼──────────┐  ┌───────────▼──────────┐
    │ LegacyOrderRepo      │  │ ModernOrderRepo      │
    │ (Entity Framework 6) │  │ (EF Core + async)    │
    └──────────────────────┘  └──────────────────────┘
```

## When to Use

- Replacing internal components (repositories, services, business logic)
- You want to avoid long-lived feature branches
- The replacement can be done incrementally while both versions coexist
- Trunk-based development workflow

## When NOT to Use

- Replacing external-facing APIs (use [Strangler Fig](../strangler-fig/README.md) instead)
- The component is trivial enough to replace in a single commit
- No clear interface boundary exists

## Implementation

### Step 1: Extract Interface

```csharp
// Create the abstraction from the existing implementation
public interface IOrderRepository
{
    Task<Order> GetByIdAsync(Guid id);
    Task<IReadOnlyList<Order>> GetByCustomerAsync(string customerId);
    Task SaveAsync(Order order);
}
```

### Step 2: Wrap Legacy Implementation

```csharp
// Legacy implementation now implements the interface
public class LegacyOrderRepository : IOrderRepository
{
    private readonly LegacyDbContext _db;

    public async Task<Order> GetByIdAsync(Guid id)
    {
        // Existing EF6 code, unchanged
        return await _db.Orders.FindAsync(id);
    }
    // ... other methods unchanged
}
```

### Step 3: Build Modern Implementation

```csharp
// New implementation behind the same interface
public class ModernOrderRepository : IOrderRepository
{
    private readonly AppDbContext _db;

    public async Task<Order> GetByIdAsync(Guid id)
    {
        // EF Core with modern patterns
        return await _db.Orders
            .AsNoTracking()
            .FirstOrDefaultAsync(o => o.Id == id);
    }
    // ... modern implementations
}
```

### Step 4: Feature Flag Toggle

```csharp
// In DI registration
if (featureFlags.IsEnabled("UseModernOrderRepo"))
{
    services.AddScoped<IOrderRepository, ModernOrderRepository>();
}
else
{
    services.AddScoped<IOrderRepository, LegacyOrderRepository>();
}
```

### Step 5: Verify and Clean Up

- Enable the flag in staging, run parity tests
- Enable in production with monitoring
- Once stable, remove the legacy class and the feature flag
- The interface may remain as good design practice

## Key Principles

- **Both implementations always compile** — No broken builds on main
- **Feature flag, not branch** — Switch at runtime, not at merge time
- **Incremental migration** — Migrate method by method if needed
- **Clean up promptly** — Remove the legacy path once verified

## Comparison with Strangler Fig

| Aspect | Branch by Abstraction | Strangler Fig |
|--------|---------------------|---------------|
| Scope | Internal components | External APIs |
| Mechanism | Interface + DI | Routing / proxy |
| Granularity | Method-level | Endpoint-level |
| Location | Inside the codebase | At the network boundary |

## Related Patterns

- [Strangler Fig](../strangler-fig/README.md) — External equivalent at the API boundary
- [Anti-Corruption Layer](../anti-corruption-layer/README.md) — Keeps legacy models from leaking during transition
