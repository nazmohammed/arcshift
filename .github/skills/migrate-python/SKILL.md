---
name: migrate-python
description: "Guided Flask to FastAPI migration workflow. Use when: converting Flask routes to FastAPI, migrating sync to async handlers, upgrading SQLAlchemy 1.x to 2.0, replacing manual validation with Pydantic models, modernising Python web applications."
---

# Flask → FastAPI Migration Workflow

Step-by-step workflow for migrating Flask applications to FastAPI with modern async patterns.

## When to Use

- Migrating Flask applications to FastAPI
- Converting synchronous handlers to async
- Upgrading SQLAlchemy 1.x to 2.0 patterns
- Replacing manual validation with Pydantic v2 models
- Modernising Python web application architecture

## Prerequisites

- Assessment report from `/assess-codebase` or @assess
- Architecture design from @architect (if decomposing)
- Python 3.11+ installed

## Procedure

### Step 1: Update Dependencies

**Before** (`requirements.txt`):
```
Flask==1.1.4
Flask-SQLAlchemy==2.5.1
Flask-WTF==0.15.1
SQLAlchemy==1.4.46
marshmallow==3.14.0
gunicorn==20.1.0
```

**After** (`requirements.txt`):
```
fastapi==0.111.0
uvicorn[standard]==0.30.0
sqlalchemy[asyncio]==2.0.30
pydantic==2.7.0
pydantic-settings==2.3.0
alembic==1.13.0
httpx==0.27.0
```

### Step 2: Convert Routes

**Before** (Flask):
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/products', methods=['GET'])
def get_products():
    category = request.args.get('category')
    products = Product.query.filter_by(category=category).all()
    return jsonify([p.to_dict() for p in products])

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.get_json()
    product = Product(name=data['name'], price=data['price'])
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201
```

**After** (FastAPI):
```python
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/api/products", tags=["products"])

@router.get("/", response_model=list[ProductResponse])
async def get_products(
    category: str | None = Query(None),
    db: AsyncSession = Depends(get_db),
):
    stmt = select(Product).where(Product.category == category) if category else select(Product)
    result = await db.execute(stmt)
    return result.scalars().all()

@router.post("/", response_model=ProductResponse, status_code=201)
async def create_product(
    product_in: ProductCreate,
    db: AsyncSession = Depends(get_db),
):
    product = Product(**product_in.model_dump())
    db.add(product)
    await db.commit()
    await db.refresh(product)
    return product
```

### Step 3: Create Pydantic Models

**Before** (manual validation or marshmallow):
```python
def validate_product(data):
    if not data.get('name'):
        raise ValueError('Name is required')
    if not isinstance(data.get('price'), (int, float)):
        raise ValueError('Price must be a number')
```

**After** (Pydantic v2):
```python
from pydantic import BaseModel, Field

class ProductCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    price: float = Field(..., gt=0)
    category: str | None = None

class ProductResponse(ProductCreate):
    id: int

    model_config = {"from_attributes": True}
```

### Step 4: Migrate SQLAlchemy to 2.0

**Before** (1.x legacy style):
```python
products = Product.query.filter_by(category=category).all()
product = Product.query.get(product_id)
```

**After** (2.0 style):
```python
from sqlalchemy import select

stmt = select(Product).where(Product.category == category)
result = await session.execute(stmt)
products = result.scalars().all()

stmt = select(Product).where(Product.id == product_id)
result = await session.execute(stmt)
product = result.scalar_one_or_none()
```

### Step 5: Add Dependency Injection

**Before** (Flask globals):
```python
from flask import g
from myapp import db

def get_current_user():
    return g.user
```

**After** (FastAPI Depends):
```python
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session

async def get_current_user(
    db: AsyncSession = Depends(get_db),
) -> User:
    # auth logic here
    ...
```

### Step 6: Migrate Configuration

**Before** (Flask):
```python
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
```

**After** (Pydantic Settings):
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    secret_key: str
    debug: bool = False

    model_config = {"env_file": ".env"}

settings = Settings()
```

### Step 7: Create Application Entry Point

**After** (`main.py`):
```python
from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    await init_db()
    yield
    # shutdown
    await close_db()

app = FastAPI(title="Atlas Inventory API", lifespan=lifespan)
app.include_router(products_router)
app.include_router(orders_router)
```

### Step 8: Verify

1. Run `pip install -r requirements.txt`
2. Run `uvicorn main:app --reload` — verify startup
3. Check `/docs` — FastAPI auto-generates OpenAPI docs
4. Run `pytest` — ensure tests pass
5. Hand off to @validate for parity testing
