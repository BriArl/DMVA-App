from fastapi import APIRouter, File, UploadFile, Query, HTTPException
from app.services.cloudinary_service import upload_image

router = APIRouter()

@router.post("/upload")
async def upload(
    file: UploadFile = File(...),
    folder: str = Query("products", description="Folder to upload to in Cloudinary")
):
    image_url = upload_image(file.file, folder=folder)
    return {"image_url": image_url}

@router.post("/moodboards")
async def upload_moodboard_image(file: UploadFile = File(...)):
    try:
        image_url = upload_image(file.file, folder="moodboards")
        return {"image_url": image_url}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image upload failed: {str(e)}")
