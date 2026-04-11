"""
Legacy SQLAlchemy 1.x models — no type hints, imperative style.
"""
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    sku = db.Column(db.String(50), unique=True, nullable=False)
    stock_quantity = db.Column(db.Integer, default=0)
    category = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    transactions = db.relationship("InventoryTransaction", backref="product")


class InventoryTransaction(db.Model):
    __tablename__ = "inventory_transactions"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity_change = db.Column(db.Integer, nullable=False)
    reason = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
