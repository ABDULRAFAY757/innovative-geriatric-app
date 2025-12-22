from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime
from .database import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    password_hash = Column(String)   # store hashed password
    role = Column(String)  # PATIENT, FAMILY, DOCTOR
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date_of_birth = Column(String)
    medical_history_summary = Column(String)
    emergency_contact = Column(String)
    user = relationship("User", back_populates="patients")
    medications = relationship("Medication", back_populates="patient")

<<<<<<< Updated upstream
class Medication(Base):
    __tablename__ = "medications"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    name = Column(String)
    dosage = Column(String)
    frequency = Column(String)
    instructions = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    patient = relationship("Patient", back_populates="medications")
=======
class Doctor(BaseModel):
    id: Optional[str] = Field(None)
    name: str
    phone: str
    email: EmailStr
    specialization: str
    availability: str
    plan: Plan


# ---------------- Symptoms ----------------
class Symptom(BaseModel):
    id: Optional[str] = Field(None)
    code: str            # e.g., SYM001
    name: str
    description: Optional[str] = None

# ---------------- Medications ----------------
class Medication(BaseModel):
    id: Optional[str] = Field(None)
    name: str
    dosage: Optional[str] = None     # e.g., 500mg
    frequency: Optional[str] = None  # e.g., Twice daily
    duration_days: Optional[int] = None
>>>>>>> Stashed changes
