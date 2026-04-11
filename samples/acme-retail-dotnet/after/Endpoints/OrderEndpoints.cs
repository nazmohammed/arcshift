using AcmeRetail.Api.Data;
using AcmeRetail.Api.Models;
using Microsoft.EntityFrameworkCore;

namespace AcmeRetail.Api.Endpoints;

public static class OrderEndpoints
{
    public static void MapOrderEndpoints(this WebApplication app)
    {
        var group = app.MapGroup("/api/orders").RequireAuthorization();

        group.MapGet("/", async (RetailDbContext db) =>
        {
            var orders = await db.Orders
                .AsNoTracking()
                .Include(o => o.OrderItems)
                .OrderByDescending(o => o.OrderDate)
                .Take(100)
                .ToListAsync();

            return Results.Ok(orders);
        })
        .WithName("GetOrders")
        .Produces<List<Order>>(200);

        group.MapGet("/{id:guid}", async (Guid id, RetailDbContext db) =>
        {
            var order = await db.Orders
                .AsNoTracking()
                .Include(o => o.OrderItems)
                .FirstOrDefaultAsync(o => o.Id == id);

            return order is null ? Results.NotFound() : Results.Ok(order);
        })
        .WithName("GetOrder")
        .Produces<Order>(200)
        .Produces(404);

        group.MapPost("/", async (CreateOrderRequest request, RetailDbContext db) =>
        {
            var order = new Order
            {
                Id = Guid.NewGuid(),
                CustomerId = request.CustomerId,
                OrderDate = DateTimeOffset.UtcNow,
                Status = OrderStatus.Pending,
                TotalAmount = request.Items.Sum(i => i.Quantity * i.UnitPrice),
                OrderItems = request.Items.Select(i => new OrderItem
                {
                    Id = Guid.NewGuid(),
                    ProductId = i.ProductId,
                    Quantity = i.Quantity,
                    UnitPrice = i.UnitPrice,
                }).ToList(),
            };

            db.Orders.Add(order);
            await db.SaveChangesAsync();

            return Results.Created($"/api/orders/{order.Id}", order);
        })
        .WithName("CreateOrder")
        .Produces<Order>(201)
        .ProducesValidationProblem();
    }
}
