# Event-Driven Decomposition Pattern

## Intent

Use domain events to decouple services during and after monolith decomposition, enabling asynchronous communication and independent scaling without direct service-to-service calls.

## Problem

When extracting services from a monolith, synchronous API calls between services create temporal coupling — if one service is down, the caller fails. Shared databases create data coupling. You need a way for services to communicate and stay consistent without being tightly bound.

## Solution

Publish domain events when state changes occur. Other services subscribe to relevant events and react independently. This replaces direct calls and shared database queries with an event-driven architecture.

```
┌──────────┐  OrderPlaced  ┌──────────────┐
│  Order   │──────────────▶│  Event Bus   │
│ Service  │               │ (Service Bus)│
└──────────┘               └──────┬───────┘
                                  │
                    ┌─────────────┼─────────────┐
                    │             │             │
              ┌─────▼────┐ ┌─────▼────┐ ┌─────▼────┐
              │Inventory │ │ Billing  │ │Notifica- │
              │ Service  │ │ Service  │ │tion Svc  │
              └──────────┘ └──────────┘ └──────────┘
              Reserve stock  Charge card  Send email
```

## When to Use

- Services need to react to changes in other services
- Operations span multiple services (choreography over orchestration)
- You need to maintain read models or projections across boundaries
- Temporal coupling is unacceptable (fire-and-forget semantics)

## When NOT to Use

- Request-response is required (client needs immediate result)
- Strict ordering guarantees are critical and hard to enforce
- The team lacks experience with eventual consistency patterns

## Event Design

### Domain Event Structure

```python
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class OrderPlaced(BaseModel):
    event_id: UUID
    event_type: str = "OrderPlaced"
    timestamp: datetime
    order_id: UUID
    customer_id: str
    total_amount: float
    line_items: list[dict]
```

### Event Naming Conventions

- Use past tense: `OrderPlaced`, `InventoryReserved`, `PaymentCharged`
- Include the aggregate: `Order.Placed` not just `Placed`
- Version events: `OrderPlaced.v1`, `OrderPlaced.v2`

## Implementation with Azure Service Bus

### Publisher

```python
from azure.servicebus.aio import ServiceBusClient
import json

async def publish_event(event: OrderPlaced):
    async with ServiceBusClient.from_connection_string(conn_str) as client:
        sender = client.get_topic_sender("order-events")
        message = ServiceBusMessage(
            body=event.model_dump_json(),
            content_type="application/json",
            subject=event.event_type,
            message_id=str(event.event_id),
        )
        await sender.send_messages(message)
```

### Subscriber

```python
async def handle_order_placed(event: OrderPlaced):
    """Inventory service reacts to OrderPlaced by reserving stock."""
    for item in event.line_items:
        await inventory_repo.reserve(
            product_id=item["product_id"],
            quantity=item["quantity"],
            order_id=event.order_id,
        )
```

## Decomposition Steps

1. **Identify domain events** in the monolith (state changes that other modules react to)
2. **Publish events** from the monolith before extracting services (dual-write phase)
3. **Build consumers** in the new service that subscribe to events
4. **Switch the consumer** from direct DB query to event-driven projection
5. **Remove the direct coupling** once the event-driven path is verified

## Patterns for Consistency

| Pattern | Use Case |
|---------|---------|
| Outbox | Ensure event is published when DB transaction commits |
| Idempotent Consumer | Handle duplicate event delivery safely |
| Dead Letter Queue | Capture failed events for retry/investigation |
| Event Sourcing | Full audit trail and temporal queries |

## Related Patterns

- [Database per Service](../database-per-service/README.md) — Events sync data across service-owned stores
- [Strangler Fig](../strangler-fig/README.md) — Events enable gradual migration of reactive workflows
