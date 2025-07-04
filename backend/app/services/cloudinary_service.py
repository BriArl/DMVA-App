import os
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", "..", ".env"))

def upload_image(file, folder="products"):
    result = cloudinary.uploader.upload(file, folder=folder)
    return result.get("secure_url")