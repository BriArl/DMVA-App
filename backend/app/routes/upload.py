from fastapi import APIRouter, File, UploadFile, Query
from app.services.cloudinary_service import upload_image

router = APIRouter()

@router.post("/upload")
async def upload(
    file: UploadFile = File(...),
    folder: str = Query("products", description="Folder to upload to in Cloudinary")
):
    image_url = upload_image(file.file, folder=folder)
    return {"image_url": image_url}