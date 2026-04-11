using AcmeRetail.Api.Data;
using AcmeRetail.Api.Endpoints;
using Microsoft.EntityFrameworkCore;
using Microsoft.Identity.Web;

var builder = WebApplication.CreateBuilder(args);

// Authentication — Entra ID
builder.Services.AddMicrosoftIdentityWebApiAuthentication(builder.Configuration);

// Database — EF Core with async
builder.Services.AddDbContext<RetailDbContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("RetailConnection")));

// OpenAPI
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

// Observability
builder.Services.AddApplicationInsightsTelemetry();
builder.Services.AddHealthChecks()
    .AddDbContextCheck<RetailDbContext>();

var app = builder.Build();

// Middleware
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseAuthentication();
app.UseAuthorization();
app.MapHealthChecks("/health");

// Endpoints
app.MapOrderEndpoints();
app.MapProductEndpoints();

app.Run();
