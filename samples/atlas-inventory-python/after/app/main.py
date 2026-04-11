"""
Modern FastAPI application for Atlas Inventory.
Demonstrates: async routes, Pydantic models, DI, structured logging.
"""
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import engine, Base
from app.routers import products, inventory


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()


app = FastAPI(
    title="Atlas Inventory API",
    version="2.0.0",
    lifespan=lifespan,
)

app.include_router(products.router, prefix="/api/products", tags=["products"])
app.include_router(inventory.router, prefix="/api/inventory", tags=["inventory"])


@app.get("/health")
async def health():
    return {"status": "healthy"}
