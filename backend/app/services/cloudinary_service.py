import os
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", "..", ".env"))

def upload_image(file):
    result = cloudinary.uploader.upload(file)
    return result.get("secure_url")