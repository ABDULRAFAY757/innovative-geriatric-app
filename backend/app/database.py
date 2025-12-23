from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings
# Example inside app/database.py
from .config import settings

client = AsyncIOMotorClient(settings.MONGODB_URL)

db = client[settings.DATABASE_NAME]

patient_collection = db["patients"]
doctor_collection = db["doctors"]
