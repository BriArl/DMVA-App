from fastapi import APIRouter, File, UploadFile
from app.services.cloudinary_service import upload_image

router = APIRouter()

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    image_url = upload_image(file.file)
    return {"image_url": image_url}