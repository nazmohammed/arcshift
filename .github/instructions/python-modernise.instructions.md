---
description: "Best practices for migrating Python web applications to FastAPI. Loaded automatically when editing Python files."
applyTo: "**/*.py"
---

# Python Modernisation Patterns

When working with Python code in this repository, follow these modernisation patterns:

## Framework Conventions
- Use FastAPI with `APIRouter` for route organisation
- Use `async def` for all route handlers and I/O operations
- Use Pydantic v2 models for request/response validation
- Use `Depends()` for dependency injection
- Use `lifespan` context manager for startup/shutdown

## Data Models
- Use Pydantic `BaseModel` for API schemas with `Field()` validators
- Use `model_config = {"from_attributes": True}` for ORM model conversion
- Separate input models (`Create`, `Update`) from response models (`Response`)
- Use `pydantic-settings` `BaseSettings` for configuration

## Data Access
- Use SQLAlchemy 2.0 style: `select()`, `insert()`, `update()`, `delete()`
- Use `AsyncSession` with `async_session_factory` for async database access
- Never use legacy `Query` API (`Model.query.filter_by()`)
- Use Alembic for database migrations

## Error Handling
- Use FastAPI exception handlers (`@app.exception_handler`)
- Use `HTTPException` with appropriate status codes
- Return structured error responses with `detail` field

## Project Structure
```
service_name/
├── main.py              # FastAPI app + lifespan
├── config.py            # Pydantic BaseSettings
├── models/              # SQLAlchemy models
├── schemas/             # Pydantic request/response models
├── routers/             # APIRouter modules
├── services/            # Business logic
├── dependencies.py      # Shared Depends() functions
└── tests/
    ├── conftest.py      # Fixtures
    └── test_*.py        # Test modules
```

## Testing
- Use `pytest` with `pytest-asyncio`
- Use `httpx.AsyncClient` with `ASGITransport` for API testing
- Use fixtures for database sessions and test data
- Mirror source structure with `test_` prefix
