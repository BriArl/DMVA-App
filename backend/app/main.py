from fastapi import FastAPI
from app.routes import products, upload

app = FastAPI()

app.include_router(products.router)
app.include_router(upload.router)