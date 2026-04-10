---
mode: "agent"
description: "Analyse legacy database schema and generate migration strategy for modernised architecture"
---

# Analyse Database Schema

Analyse the database schema for **{{database_name}}** and produce a migration strategy aligned with the target architecture.

## Schema Discovery

1. List all tables, views, stored procedures, and functions
2. Map foreign key relationships and dependency graph
3. Identify clustered/non-clustered indexes and their usage patterns
4. Document triggers, computed columns, and database-level business logic
5. Measure table sizes (row counts, storage) where available

## Schema Assessment

| Table | Row Count | Relationships | Business Logic | Bounded Context | Migration Complexity |
|-------|-----------|--------------|----------------|-----------------|---------------------|
| _name_ | _count_ | _FK count_ | _triggers/procs_ | _context_ | low/medium/high |

## Data Ownership Mapping

For each bounded context identified:
- Tables owned exclusively by this context
- Tables shared across contexts (requires decomposition)
- Read-only references to other contexts' data

## Migration Strategy

### Option A: Lift and Shift
- Migrate schema as-is to Azure SQL / PostgreSQL
- Refactor stored procedures to application code post-migration

### Option B: Database per Service
- Split schema along bounded context boundaries
- Define data synchronisation strategy (events, CDC, ETL)
- Generate migration scripts per service

### Option C: Polyglot Persistence
- Map each context to optimal data store (SQL, CosmosDB, Redis, Blob)
- Define data access patterns per context

## Output

Deliver:
- Entity-relationship diagram (Mermaid)
- Table-to-context mapping
- Recommended migration option with justification
- Migration scripts (DDL for target schema)
- Data migration runbook (sequence, rollback steps)
