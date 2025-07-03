from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    sku: str
    color: Optional[str]
    image_url: Optional[str]