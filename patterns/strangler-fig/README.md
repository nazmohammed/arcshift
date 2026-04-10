# Strangler Fig Pattern

## Intent

Incrementally replace a legacy system by routing traffic through a facade that gradually delegates to the modernised implementation, avoiding big-bang migrations.

## Problem

Rewriting a legacy system from scratch is high-risk: it takes months or years, feature parity is hard to achieve, and the business can't stop while the replacement is built. You need a way to migrate incrementally while keeping the legacy system running.

## Solution

Place a routing layer (facade) in front of the legacy system. As each component is modernised, update the routing to direct traffic to the new implementation. The legacy system gradually "withers" as more routes are migrated.

```
                    ┌──────────────┐
      Requests ────▶│   Facade /   │
                    │    Router    │
                    └──────┬───────┘
                           │
                ┌──────────┼──────────┐
                │          │          │
           ┌────▼────┐ ┌───▼────┐ ┌──▼──────┐
           │ Modern  │ │ Modern │ │ Legacy  │
           │Service A│ │Svc B   │ │ System  │
           └─────────┘ └────────┘ └─────────┘
```

## When to Use

- Migrating a monolith to microservices
- Replacing legacy APIs with modern equivalents
- Gradual framework upgrades (e.g., .NET Framework → .NET 8)

## When NOT to Use

- The legacy system is small enough for a full rewrite in one sprint
- No clear API boundary exists to place a facade
- The system will be decommissioned entirely (no migration needed)

## Implementation

### 1. Create the Facade
- Deploy a reverse proxy or API gateway (Azure API Management, YARP, nginx)
- Route all traffic through the facade to the legacy system initially

### 2. Migrate One Route
- Implement the first endpoint in the modern service
- Update the facade to route that path to the new service
- Keep the legacy route as a fallback

### 3. Add Feature Flags
```python
# Facade routing with feature flag
if feature_flags.is_enabled("orders_v2"):
    response = await new_order_service.get_orders(request)
else:
    response = await legacy_system.get_orders(request)
```

### 4. Monitor and Compare
- Log responses from both old and new paths (shadow traffic)
- Compare latency, error rates, and response bodies
- Proceed to next route only when parity is confirmed

### 5. Decommission Legacy Routes
- Once all routes are migrated, remove the legacy system
- Clean up feature flags and dual-routing logic

## Azure Implementation

| Component | Azure Service |
|-----------|--------------|
| Facade / Router | Azure API Management or Azure Front Door |
| Modern Services | Azure Container Apps |
| Feature Flags | Azure App Configuration |
| Monitoring | Application Insights |

## Related Patterns

- [Anti-Corruption Layer](../anti-corruption-layer/README.md) — Protects modern code from legacy data models
- [Branch by Abstraction](../branch-by-abstraction/README.md) — In-code equivalent for internal refactoring
