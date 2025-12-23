import motor.motor_asyncio
from app.config import settings
import certifi

client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.MONGO_URI,
    tlsCAFile=certifi.where()
)

db = client[settings.DATABASE_NAME]

patient_collection = db["patients"]
doctor_collection = db["doctors"]
