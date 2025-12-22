from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/medical"

<<<<<<< Updated upstream
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
=======
db = client["healthcare_db"]

patient_collection = db["patients"]
doctor_collection = db["doctors"]
symptom_collection = db["symptoms"]
medication_collection = db["medications"]

def serialize(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc
>>>>>>> Stashed changes
