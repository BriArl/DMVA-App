import os
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", "..", ".env"))

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECERT")
)

def upload_image(file):
    result = cloudinary.uploader.upload(file)
    return result.get("secure_url")