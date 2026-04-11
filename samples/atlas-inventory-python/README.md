# Atlas Inventory — Python Sample

A representative Flask → FastAPI modernisation sample demonstrating Arcshift methodology.

## Structure

```
atlas-inventory-python/
  before/     ← Legacy Flask + SQLAlchemy 1.x
  after/      ← Modernised FastAPI + SQLAlchemy 2.0 + async
```

## Scenario

Atlas Inventory manages warehouse stock levels with:
- Flask with Jinja2 templates
- SQLAlchemy 1.x with synchronous sessions
- Basic API key authentication
- Manual JSON serialisation
- Deployed on VM with gunicorn

## Migration Target

- FastAPI with Pydantic models
- SQLAlchemy 2.0 with async sessions
- Entra ID authentication (MSAL)
- Automatic OpenAPI documentation
- Container Apps hosting with uvicorn

## How to Use

1. Run `@assess` on the `before/` directory
2. Run `@architect` to design the target architecture
3. Run `@migrate` to transform the code into `after/`
4. Run `@validate` to verify parity
5. Run `@deploy` to generate IaC and deploy
