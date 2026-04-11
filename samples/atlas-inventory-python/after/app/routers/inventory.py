"""Modern FastAPI router for inventory adjustments with async DB."""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Product, InventoryTransaction

router = APIRouter()


class AdjustInventoryRequest(BaseModel):
    product_id: str
    quantity_change: int
    reason: str = "Manual adjustment"


class AdjustInventoryResponse(BaseModel):
    product_id: str
    new_stock: int


@router.post("/adjust", response_model=AdjustInventoryResponse)
async def adjust_inventory(
    request: AdjustInventoryRequest,
    session: AsyncSession = Depends(get_session),
):
    result = await session.execute(
        select(Product).where(Product.id == request.product_id)
    )
    product = result.scalar_one_or_none()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    product.stock_quantity += request.quantity_change

    transaction = InventoryTransaction(
        product_id=product.id,
        quantity_change=request.quantity_change,
        reason=request.reason,
    )
    session.add(transaction)
    await session.commit()
    await session.refresh(product)

    return AdjustInventoryResponse(
        product_id=product.id, new_stock=product.stock_quantity
    )
