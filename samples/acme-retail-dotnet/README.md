# Acme Retail — .NET Sample

A representative .NET Framework 4.8 → .NET 8 modernisation sample demonstrating Arcshift methodology.

## Structure

```
acme-retail-dotnet/
  before/     ← Legacy .NET Framework 4.8 MVC + Web API
  after/      ← Modernised .NET 8 Minimal API + Container Apps
```

## Scenario

Acme Retail operates a monolithic e-commerce application built on:
- ASP.NET MVC 5 with Razor views
- ASP.NET Web API 2 for REST endpoints
- Entity Framework 6 with SQL Server
- Windows Authentication
- IIS hosting with web.config

## Migration Target

- ASP.NET Core 8 Minimal API
- Entity Framework Core 8 with async patterns
- Entra ID authentication (MSAL)
- Container Apps hosting
- appsettings.json + Azure App Configuration

## How to Use

1. Run `@assess` on the `before/` directory to generate an assessment
2. Run `@architect` to design the target architecture
3. Run `@migrate` to transform the code into `after/`
4. Run `@validate` to verify parity between before and after
5. Run `@deploy` to generate IaC and deploy to Azure
