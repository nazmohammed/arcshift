---
description: "Best practices for migrating .NET Framework code to .NET 8. Loaded automatically when editing C# or project files."
applyTo: "**/*.cs,**/*.csproj"
---

# .NET Modernisation Patterns

When working with .NET code in this repository, follow these modernisation patterns:

## Project File Conventions
- Use SDK-style `.csproj` with `<TargetFramework>net8.0</TargetFramework>`
- Enable nullable reference types: `<Nullable>enable</Nullable>`
- Enable implicit usings: `<ImplicitUsings>enable</ImplicitUsings>`
- Use `<PackageReference>` instead of `packages.config`

## Code Patterns
- Use minimal hosting (`WebApplication.CreateBuilder`) instead of `Startup.cs`
- Use built-in DI (`builder.Services.AddScoped<T>()`) instead of third-party containers
- Use `IConfiguration` and `IOptions<T>` instead of `ConfigurationManager`
- Use `System.Text.Json` by default; only use `Newtonsoft.Json` for complex polymorphic serialisation
- Use `ILogger<T>` instead of `log4net` / `NLog` / `Console.WriteLine`

## Data Access
- Use EF Core with `DbContextOptions<T>` constructor pattern
- Use `select()` LINQ expressions with `async/await`
- Configure via `builder.Services.AddDbContext<T>()`
- Run migrations with `dotnet ef migrations add` / `dotnet ef database update`

## API Patterns
- Use `[ApiController]` attribute on controllers
- Use `ControllerBase` instead of `Controller` for API-only controllers
- Use model binding (`[FromBody]`, `[FromQuery]`, `[FromRoute]`) instead of manual parsing
- Return `ActionResult<T>` for typed responses

## Authentication
- Use ASP.NET Core Identity for local auth
- Use `Microsoft.Identity.Web` for Entra ID / Azure AD integration
- Use `[Authorize]` attribute instead of custom auth filters

## Testing
- Use xUnit with `FluentAssertions`
- Use `WebApplicationFactory<T>` for integration tests
- Mirror source structure in test projects
