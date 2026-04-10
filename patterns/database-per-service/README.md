# Database per Service Pattern

## Intent

Give each microservice its own private data store, ensuring loose coupling, independent deployability, and technology freedom for persistence.

## Problem

In a monolith, all components share a single database. This creates tight coupling: schema changes affect every component, scaling requires scaling the entire database, and teams can't choose the best storage technology for their use case.

## Solution

Each service owns its data exclusively. No other service accesses another service's database directly — all data sharing happens through well-defined APIs or events.

```
┌──────────┐  ┌──────────┐  ┌──────────┐
│ Order    │  │ Inventory│  │ Customer │
│ Service  │  │ Service  │  │ Service  │
└────┬─────┘  └────┬─────┘  └────┬─────┘
     │             │             │
┌────▼─────┐  ┌────▼─────┐  ┌────▼─────┐
│ Order DB │  │Inventory │  │Customer  │
│(Azure SQL)│  │(CosmosDB)│  │(Postgres)│
└──────────┘  └──────────┘  └──────────┘
```

## When to Use

- Decomposing a shared database across service boundaries
- Services have different data access patterns (relational vs. document vs. key-value)
- Teams need to evolve schemas independently

## When NOT to Use

- Monolith with shared transactions that can't be decomposed yet
- Strong consistency requirements across services (consider Saga pattern instead)
- Very small application where a shared database adds no coupling risk

## Data Decomposition Strategy

### Step 1: Identify Table Ownership
Map each table to its owning bounded context:

| Table | Owner Service | Shared By | Action |
|-------|--------------|-----------|--------|
| Orders | Order Service | — | Move to Order DB |
| OrderItems | Order Service | — | Move to Order DB |
| Products | Inventory Service | Order Service (read) | Move to Inventory DB, expose API |
| Customers | Customer Service | Order Service (FK) | Move to Customer DB, expose API |

### Step 2: Replace Foreign Keys with API Calls

```python
# Before: Direct FK join
SELECT o.*, c.Name FROM Orders o JOIN Customers c ON o.CustomerId = c.Id

# After: API call from Order Service
order = await order_repo.get(order_id)
customer = await customer_service_client.get(order.customer_id)
```

### Step 3: Handle Cross-Service Queries
- **API Composition**: Query multiple services and join in memory
- **CQRS Read Model**: Maintain a denormalised read-only projection
- **Event-Driven Sync**: Publish domain events, consume and materialise views

### Step 4: Manage Distributed Transactions
- Replace ACID transactions with the **Saga pattern**
- Use compensating actions for rollback
- Accept eventual consistency where possible

## Data Migration Sequence

1. Create the new service-specific database
2. Migrate the schema (tables, indexes, constraints)
3. Set up dual-write or CDC replication from the shared DB
4. Switch the service to read from the new database
5. Switch the service to write to the new database
6. Verify data consistency
7. Remove the old tables from the shared database

## Related Patterns

- [Anti-Corruption Layer](../anti-corruption-layer/README.md) — Translate between old and new data models
- [Event-Driven Decomposition](../event-driven-decomposition/README.md) — Sync data across service boundaries via events
