from fastapi import APIRouter, HTTPException
from app.models.moodboard import Moodboard
from app.config import db
from datetime import datetime

router = APIRouter()
moodboards_collection = db["moodboards"]

@router.post("/")
async def create_moodboard(moodboard: Moodboard):
    moodboard_data = moodboard.dict()
    moodboard_data["created_at"] = datetime.utcnow()

    result = await moodboards_collection.insert_one(moodboard_data)
    return {"id": str(result.inserted_id), "message": "Moodboard created"}

@router.get("/")
async def get_moodboards():
    moodboards = []
    cursor = moodboards_collection.find({})
    async for moodboard in cursor:
        moodboard["id"] = str(moodboard["_id"])
        moodboards.append(moodboard)
    return moodboards