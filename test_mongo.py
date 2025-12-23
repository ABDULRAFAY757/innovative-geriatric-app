import asyncio
from app.config import settings
import motor.motor_asyncio
import certifi

client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.MONGO_URI,
    tlsCAFile=certifi.where()
)
db = client[settings.DATABASE_NAME]

async def test():
    try:
        info = await db.list_collection_names()
        print("✅ Connected! Collections:", info)
    except Exception as e:
        print("❌ Connection failed:", e)

asyncio.run(test())
