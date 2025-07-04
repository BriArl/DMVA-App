from fastapi import FastAPI
from app.routes import products, upload, moodboards

app = FastAPI()

app.include_router(products.router, prefix="/products")
app.include_router(upload.router, prefix="/upload")
app.include_router(moodboards.router, prefix="/moodboard")