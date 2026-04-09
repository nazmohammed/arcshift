---
name: migrate-dotnet
description: "Guided .NET Framework to .NET 8 migration workflow. Use when: converting .NET Framework 4.x projects to .NET 8, upgrading csproj files, migrating Startup.cs to minimal hosting, converting EF6 to EF Core, updating NuGet packages, modernising ASP.NET MVC to ASP.NET Core."
---

# .NET Framework → .NET 8 Migration Workflow

Step-by-step workflow for migrating .NET Framework 4.x applications to .NET 8 with modern patterns.

## When to Use

- Migrating ASP.NET MVC / Web API from .NET Framework to .NET 8
- Converting EF6 data access to EF Core
- Updating legacy NuGet packages to modern equivalents
- Converting `Startup.cs` + `Global.asax` to minimal hosting `Program.cs`

## Prerequisites

- Assessment report from `/assess-codebase` or @assess
- Architecture design from @architect (if decomposing)
- .NET 8 SDK installed

## Procedure

### Step 1: Convert Project File

Convert old-format `.csproj` to SDK-style:

**Before** (.NET Framework):
```xml
<?xml version="1.0" encoding="utf-8"?>
<Project ToolsVersion="15.0" DefaultTargets="Build" xmlns="...">
  <PropertyGroup>
    <TargetFrameworkVersion>v4.8</TargetFrameworkVersion>
    ...hundreds of lines...
  </PropertyGroup>
  <ItemGroup>
    <Reference Include="System.Web" />
    ...
  </ItemGroup>
</Project>
```

**After** (.NET 8):
```xml
<Project Sdk="Microsoft.NET.Sdk.Web">
  <PropertyGroup>
    <TargetFramework>net8.0</TargetFramework>
    <Nullable>enable</Nullable>
    <ImplicitUsings>enable</ImplicitUsings>
  </PropertyGroup>
</Project>
```

### Step 2: Update NuGet Packages

| Legacy Package | Modern Replacement |
|---------------|-------------------|
| `Microsoft.AspNet.WebApi` | `Microsoft.AspNetCore.Mvc` (built-in) |
| `Microsoft.AspNet.Mvc` | `Microsoft.AspNetCore.Mvc` (built-in) |
| `EntityFramework` (EF6) | `Microsoft.EntityFrameworkCore` |
| `Newtonsoft.Json` | `System.Text.Json` (or keep if complex) |
| `Microsoft.Owin` | Built-in middleware pipeline |
| `Unity` / `Autofac` | Built-in DI (`Microsoft.Extensions.DependencyInjection`) |
| `log4net` / `NLog` | `Microsoft.Extensions.Logging` |
| `Microsoft.AspNet.Identity` | `Microsoft.AspNetCore.Identity` |

### Step 3: Migrate Entry Point

**Before** (`Global.asax.cs` + `Startup.cs`):
```csharp
public class MvcApplication : System.Web.HttpApplication
{
    protected void Application_Start()
    {
        AreaRegistration.RegisterAllAreas();
        GlobalConfiguration.Configure(WebApiConfig.Register);
        FilterConfig.RegisterGlobalFilters(GlobalFilters.Filters);
        RouteConfig.RegisterRoutes(RouteTable.Routes);
    }
}
```

**After** (`Program.cs` — minimal hosting):
```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddDbContext<AppDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("Default")));

var app = builder.Build();

app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();

app.Run();
```

### Step 4: Migrate Controllers

- Remove `ApiController` base class → use `ControllerBase` with `[ApiController]`
- Replace `HttpContext.Current` → inject `IHttpContextAccessor`
- Replace `Request.QueryString` → use model binding with `[FromQuery]`
- Replace `GlobalConfiguration` → use `IOptions<T>` pattern

### Step 5: Migrate Data Access (EF6 → EF Core)

- Replace `DbContext` constructor: connection string → `DbContextOptions<T>`
- Replace `Database.SetInitializer` → EF Core migrations
- Update LINQ: `FirstOrDefaultAsync()` now requires `using Microsoft.EntityFrameworkCore`
- Replace `DbEntityValidationException` → model validation middleware
- Update navigation properties: lazy loading requires explicit opt-in in EF Core

### Step 6: Migrate Configuration

- `web.config` `<appSettings>` → `appsettings.json`
- `web.config` `<connectionStrings>` → `ConnectionStrings` section in `appsettings.json`
- `ConfigurationManager.AppSettings["key"]` → `IConfiguration["key"]` or `IOptions<T>`

### Step 7: Migrate Authentication

- Forms Authentication → ASP.NET Core Identity + cookie auth
- Windows Authentication → Negotiate/Kerberos middleware
- Custom auth → JWT Bearer tokens or Entra ID (MSAL)

### Step 8: Verify Build

1. Run `dotnet build` — fix all compilation errors
2. Run `dotnet test` — ensure existing tests pass
3. Run `dotnet run` — verify the application starts
4. Hand off to @validate for parity testing
