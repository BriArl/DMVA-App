from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.config import db
from app.services.cloudinary_service import upload_image

router = APIRouter()

products_collection = db["products"]

@router.post("/products")
async def create_product(
    name: str = Form(...),
    sku: str = Form(...),
    color: str = Form(...),
    image: UploadFile = File(...)
):
    try:
        image_url = upload_image(image.file, folder="products")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image upload failed: {str(e)}")
    
    product_data = {
        "name": name,
        "sku": sku,
        "color": color,
        "image_url": image_url
    }

    result = await products_collection.insert_one(product_data)
    return {"id": str(result.inserted_id), "message": "Product created"}

@router.get("/products")
async def get_products():
    products = []
    cursor = db["products"].find({})
    async for product in cursor:
        product["id"] = str(product["_id"])
        products.append(product)
    return products