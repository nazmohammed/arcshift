"""Modern FastAPI router for products with Pydantic schemas and async DB."""
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_session
from app.models import Product

router = APIRouter()


class ProductResponse(BaseModel):
    id: str
    name: str
    sku: str
    stock_quantity: int
    category: str | None

    model_config = {"from_attributes": True}


@router.get("/", response_model=list[ProductResponse])
async def list_products(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Product))
    return result.scalars().all()


@router.get("/{product_id}", response_model=ProductResponse)
async def get_product(product_id: str, session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Product).where(Product.id == product_id))
    product = result.scalar_one_or_none()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
