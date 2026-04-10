# API Gateway Pattern

## Intent

Provide a single entry point for all client requests, routing them to the appropriate backend services while handling cross-cutting concerns like authentication, rate limiting, and protocol translation.

## Problem

When a monolith is decomposed into microservices, clients must know about and communicate with multiple services. This creates tight coupling between clients and service topology, makes cross-cutting concerns (auth, logging, throttling) hard to enforce consistently, and exposes internal architecture.

## Solution

Deploy an API gateway as the single entry point. The gateway routes requests to backend services and handles cross-cutting concerns in one place.

```
                    ┌────────────────────────┐
   Mobile ─────────▶│                        │──▶ Order Service
   Web ────────────▶│     API Gateway        │──▶ Inventory Service
   Partner API ────▶│                        │──▶ Customer Service
                    │ • Auth  • Rate Limit   │──▶ Payment Service
                    │ • Cache • Transform    │
                    └────────────────────────┘
```

## When to Use

- Multiple client types (web, mobile, third-party) consuming backend services
- Cross-cutting concerns need centralised enforcement
- Backend service topology should be hidden from clients
- Different clients need different API shapes (BFF pattern)

## When NOT to Use

- Single service with single client type (unnecessary indirection)
- Internal service-to-service communication (use service mesh instead)
- The gateway becomes a bottleneck or single point of failure without proper scaling

## Gateway Responsibilities

| Concern | Implementation |
|---------|---------------|
| Routing | Path-based routing to backend services |
| Authentication | Validate JWT tokens, API keys |
| Rate Limiting | Per-client or per-endpoint throttling |
| Caching | Response caching for read-heavy endpoints |
| Request Transform | Aggregate, filter, or reshape responses |
| Protocol Translation | REST ↔ gRPC, WebSocket upgrade |
| Circuit Breaking | Fail fast when backend services are unhealthy |
| Observability | Request logging, distributed tracing headers |

## Azure Implementation

### Azure API Management (APIM)

```bicep
resource apiManagement 'Microsoft.ApiManagement/service@2023-09-01-preview' = {
  name: 'apim-${appName}'
  location: location
  sku: {
    name: 'Consumption'
    capacity: 0
  }
  properties: {
    publisherEmail: publisherEmail
    publisherName: publisherName
  }
}
```

### Route Configuration

```xml
<!-- APIM Policy: Route /orders/* to Order Service -->
<policies>
  <inbound>
    <set-backend-service base-url="https://order-service.internal" />
    <validate-jwt header-name="Authorization"
                  failed-validation-httpcode="401">
      <openid-config url="https://login.microsoftonline.com/{tenant}/.well-known/openid-configuration" />
    </validate-jwt>
    <rate-limit calls="100" renewal-period="60" />
  </inbound>
</policies>
```

### Backend for Frontend (BFF)

When different clients need different API shapes:
- **Web BFF**: Full payloads, pagination, complex queries
- **Mobile BFF**: Compact payloads, aggregated responses, offline-friendly
- **Partner BFF**: Versioned, stable contracts, webhook support

## Migration Strategy

1. Deploy the gateway in front of the monolith (passthrough mode)
2. As services are extracted, add routes to new services
3. The gateway absorbs cross-cutting concerns from the monolith
4. Eventually all routes point to modern services

## Related Patterns

- [Strangler Fig](../strangler-fig/README.md) — The gateway acts as the facade for incremental migration
- [Anti-Corruption Layer](../anti-corruption-layer/README.md) — Gateway can translate between client and legacy models
