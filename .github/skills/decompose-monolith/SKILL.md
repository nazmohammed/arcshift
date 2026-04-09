---
name: decompose-monolith
description: "Decompose monolithic applications into microservices. Use when: identifying bounded contexts, defining service boundaries, extracting services from a monolith, planning data decomposition, implementing strangler fig pattern, designing inter-service communication."
---

# Monolith Decomposition Workflow

Step-by-step workflow for breaking apart a monolithic application into microservices using proven decomposition patterns.

## When to Use

- Decomposing a monolith into microservices as part of modernisation
- Identifying bounded contexts and service boundaries
- Planning database decomposition from a shared database
- Implementing incremental migration with strangler fig or branch by abstraction

## Prerequisites

- Assessment report from `/assess-codebase` or @assess
- Understanding of the business domain and capabilities

## Procedure

### Step 1: Map Business Capabilities

1. List all business capabilities the monolith supports (e.g., product catalogue, order management, user auth, inventory, reporting)
2. Group related functionality — these become candidate bounded contexts
3. Identify which capabilities are core (differentiating) vs supporting (commodity)

### Step 2: Analyse Code Dependencies

1. Map which code modules/namespaces depend on each other
2. Identify clusters of tightly coupled code — these should stay together
3. Find natural seams — areas with minimal cross-cutting dependencies
4. Flag shared data models used across multiple capabilities

### Step 3: Define Service Boundaries

For each candidate service:

| Attribute | Definition |
|-----------|-----------|
| **Name** | Clear, domain-aligned name |
| **Responsibility** | Single capability or cohesive group |
| **API Surface** | What operations does it expose? |
| **Data Ownership** | What data does it own exclusively? |
| **Dependencies** | What other services does it call? |
| **Shared Data** | What data is currently shared with other services? |

### Step 4: Plan Data Decomposition

1. **Identify tables per service** — Which tables belong to which service?
2. **Handle shared tables** — Options: duplicate with sync, shared read-only view, or API calls
3. **Define data contracts** — How services exchange data (DTOs, events)
4. **Plan migration order** — Start with the least-coupled service

Data decomposition strategies:
- **Database per service** — Each service owns its database (target state)
- **Shared database, separate schemas** — Intermediate step
- **CQRS** — Separate read/write models when query patterns differ significantly

### Step 5: Design Inter-Service Communication

| Pattern | Use When |
|---------|----------|
| **Synchronous REST** | Simple request-response, low latency needed |
| **Async Events** | Decoupling, eventual consistency acceptable |
| **API Gateway** | External-facing, aggregation, auth |
| **Service Mesh** | Complex routing, observability, retries |

### Step 6: Plan Extraction Order

Apply the strangler fig pattern — extract services incrementally:

1. **Start with the least-coupled service** — Easiest extraction, proves the pattern
2. **Extract services with clear data ownership** — Minimal shared state
3. **Leave the core monolith for last** — It's the hardest and riskiest

For each extraction:
1. Create the new service alongside the monolith
2. Route new traffic to the new service
3. Migrate existing traffic gradually
4. Decommission the monolith code for that capability

### Step 7: Define Anti-Corruption Layer

Between the monolith and each extracted service:
- Adapter translates between legacy and modern data models
- Prevents legacy patterns from leaking into new services
- Can be implemented as a REST middleware, message translator, or facade

### Step 8: Generate Service Map

Produce the service map JSON following @architect's schema, annotated with:
- Extraction order (1, 2, 3...)
- Risk level per service extraction
- Data migration strategy per service
- Estimated effort (small, medium, large)

Hand off the service map to @architect for Azure service selection and ADR generation.
