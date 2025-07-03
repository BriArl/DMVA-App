from fastapi import APIRouter, HTTPException
from app.models.product import Product
from app.config import db

router = APIRouter()

@router.post("/products")
async def create_product(product: Product):
    result = await db["products"].insert_one(product.dict())
    return {"id": str(result.inserted_id), "message": "Product created"}

@router.get("/products")
async def get_products():
    products = []
    cursor = db["products"].find({})
    async for product in cursor:
        product["id"] = str(product["_id"])
        products.append(product)
    return products