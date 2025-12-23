import motor.motor_asyncio
import certifi
from app.config import settings

client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.MONGO_URI,
    tlsCAFile=certifi.where()
)
db = client[settings.DATABASE_NAME]

# Collections
patient_collection = db["patients"]
doctor_collection = db["doctors"]
symptom_collection = db["symptoms"]
medication_collection = db["medications"]
transaction_collection = db["transactions"]
patient_med_history_collection = db["patient_medication_history"]

# Utility
def serialize(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc
