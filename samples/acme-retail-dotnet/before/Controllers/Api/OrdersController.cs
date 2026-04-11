using System.Collections.Generic;
using System.Linq;
using System.Web.Http;
using AcmeRetail.Web.Data;
using AcmeRetail.Web.Models;

namespace AcmeRetail.Web.Controllers.Api
{
    /// <summary>
    /// Legacy Web API 2 controller for order management.
    /// Demonstrates synchronous data access, no DI, tight coupling to EF6.
    /// </summary>
    public class OrdersController : ApiController
    {
        private readonly RetailDbContext _db = new RetailDbContext();

        // GET api/orders
        [HttpGet]
        [Route("api/orders")]
        public IHttpActionResult GetOrders()
        {
            var orders = _db.Orders
                .Include("OrderItems")
                .Include("Customer")
                .OrderByDescending(o => o.OrderDate)
                .Take(100)
                .ToList();

            return Ok(orders);
        }

        // GET api/orders/{id}
        [HttpGet]
        [Route("api/orders/{id}")]
        public IHttpActionResult GetOrder(int id)
        {
            var order = _db.Orders
                .Include("OrderItems")
                .Include("Customer")
                .FirstOrDefault(o => o.Id == id);

            if (order == null)
                return NotFound();

            return Ok(order);
        }

        // POST api/orders
        [HttpPost]
        [Route("api/orders")]
        public IHttpActionResult CreateOrder(Order order)
        {
            if (!ModelState.IsValid)
                return BadRequest(ModelState);

            order.OrderDate = System.DateTime.Now;
            order.Status = "Pending";

            _db.Orders.Add(order);
            _db.SaveChanges();

            return Created($"api/orders/{order.Id}", order);
        }

        protected override void Dispose(bool disposing)
        {
            if (disposing)
                _db.Dispose();

            base.Dispose(disposing);
        }
    }
}
