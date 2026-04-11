"""Modern SQLAlchemy 2.0 models with mapped_column and type hints."""
from datetime import datetime
from uuid import uuid4

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = "products"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(String(200))
    sku: Mapped[str] = mapped_column(String(50), unique=True)
    stock_quantity: Mapped[int] = mapped_column(default=0)
    category: Mapped[str | None] = mapped_column(String(100))
    created_at: Mapped[datetime] = mapped_column(default_factory=datetime.utcnow)

    transactions: Mapped[list["InventoryTransaction"]] = relationship(back_populates="product")


class InventoryTransaction(Base):
    __tablename__ = "inventory_transactions"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid4()))
    product_id: Mapped[str] = mapped_column(ForeignKey("products.id"))
    quantity_change: Mapped[int]
    reason: Mapped[str | None] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(default_factory=datetime.utcnow)

    product: Mapped["Product"] = relationship(back_populates="transactions")
