from pydantic import BaseModel
from typing import Optional

class ProductCreate(BaseModel):
    name: str
    sku: str
    color: str