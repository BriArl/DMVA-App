from fastapi import APIRouter, HTTPException
from app.models.moodboard import Moodboard
from app.config import db
from datetime import datetime
from bson import ObjectId

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
        del moodboard["_id"]
        moodboards.append(moodboard)
    return moodboards

@router.get("{/id}")
async def get_moodboard_by_id(id: str):
    try:
        moodboard = await moodboards_collection.find_one({"_id": ObjectId(id)})
        if not moodboard:
            raise HTTPException(status_code=404, detail="Moodboard not found")
    
        moodboard["id"] = str(moodboard["_id"])
        del moodboard["_id"]
        return moodboard

    except Exception:
        raise HTTPException(status_code=400, detail="Invalid moodboard ID")

@router.delete("/{id}")
async def delete_moodboard(id: str):
    try:
        result = await moodboards_collection.delete_one({"_id": ObjectId(id)})
        if result.deleted_count == 0:
            raise HTTPException(status_code=404, detail="Moodboard not found")
        return {"message": "Moodboard deleted"}
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid moodboard ID")