using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace AcmeRetail.Web.Models
{
    public class Order
    {
        public int Id { get; set; }

        [Required]
        public int CustomerId { get; set; }

        public DateTime OrderDate { get; set; }

        [StringLength(50)]
        public string Status { get; set; }

        public decimal TotalAmount { get; set; }

        public virtual Customer Customer { get; set; }
        public virtual ICollection<OrderItem> OrderItems { get; set; }
    }

    public class OrderItem
    {
        public int Id { get; set; }
        public int OrderId { get; set; }
        public int ProductId { get; set; }
        public int Quantity { get; set; }
        public decimal UnitPrice { get; set; }

        public virtual Order Order { get; set; }
        public virtual Product Product { get; set; }
    }

    public class Product
    {
        public int Id { get; set; }

        [Required]
        [StringLength(200)]
        public string Name { get; set; }

        [StringLength(1000)]
        public string Description { get; set; }

        public decimal Price { get; set; }
        public int StockQuantity { get; set; }

        [StringLength(100)]
        public string Category { get; set; }
    }

    public class Customer
    {
        public int Id { get; set; }

        [Required]
        [StringLength(100)]
        public string Name { get; set; }

        [Required]
        [EmailAddress]
        [StringLength(200)]
        public string Email { get; set; }

        [StringLength(20)]
        public string Phone { get; set; }

        public virtual ICollection<Order> Orders { get; set; }
    }
}
