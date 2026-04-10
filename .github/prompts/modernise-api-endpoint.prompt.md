---
mode: "agent"
description: "Modernise a legacy API endpoint to target stack with OpenAPI contract"
---

# Modernise API Endpoint

Modernise the **{{endpoint_path}}** endpoint from the legacy stack to the target platform.

## Legacy Endpoint Analysis

1. Read the current implementation of `{{endpoint_path}}`
2. Document the HTTP method, route, query parameters, and request/response bodies
3. Identify authentication/authorisation requirements
4. List middleware, filters, or interceptors applied
5. Map downstream service and database calls

## Current Contract

```
Method:   {{http_method}}
Route:    {{endpoint_path}}
Auth:     [document current auth]
Request:  [document request schema]
Response: [document response schema]
Status:   [list all status codes returned]
```

## Modernisation Steps

### For .NET (ASP.NET → Minimal API / Controller)
1. Convert to modern controller or minimal API endpoint
2. Replace `System.Web` dependencies with `Microsoft.AspNetCore`
3. Use model binding and `[FromBody]`/`[FromQuery]` attributes
4. Add `ProducesResponseType` attributes for OpenAPI
5. Replace synchronous data access with async/await
6. Add input validation with FluentValidation or DataAnnotations

### For Python (Flask → FastAPI)
1. Convert route decorator from `@app.route` to `@router.get/post`
2. Add Pydantic request/response models with validation
3. Convert to async def with async database calls
4. Add `response_model` and status code declarations
5. Replace manual JSON parsing with automatic serialisation
6. Add dependency injection for services

## Output

Deliver:
- Modernised endpoint code
- Request/response Pydantic models or C# DTOs
- OpenAPI operation annotations
- Unit tests for the endpoint
- Migration notes (breaking changes, deprecations)
