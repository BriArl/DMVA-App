from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Moodboard(BaseModel):
    title: str
    description: Optional[str] = None
    image_urls: List[str]
    product_ids: Optional[List[str]] = []
    created_at: Optional[datetime] = None