from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from enum import Enum
from datetime import datetime

class Plan(str, Enum):
    free = "Free Plan"
    professional = "Professional Plan"

class Patient(BaseModel):
    id: Optional[str] = Field(None)
    iqaama: str
    p_no: str
    phone: str
    name: str
    email: EmailStr
    plan: Plan

class Doctor(BaseModel):
    id: Optional[str] = Field(None)
    name: str
    phone: str
    email: EmailStr
    specialization: str
    availability: str
    plan: Plan

class Symptom(BaseModel):
    id: Optional[str] = None
    symptom: str

class Medication(BaseModel):
    id: Optional[str] = None
    name: str

class Transaction(BaseModel):
    id: Optional[str] = None
    patient_id: str
    doctor_id: str
    transaction_type: str
    chief_complaint: Optional[str] = None
    clinical_notes: Optional[str] = None
    admission_required: bool = False
    hospital_days: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class MedicationEntry(BaseModel):
    medication_id: str
    name: str
    dose: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

class PatientMedicationHistory(BaseModel):
    id: Optional[str] = Field(None)
    patient_id: str
    doctor_id: str
    medications: List[MedicationEntry]
    notes: Optional[str] = None
    transaction_id: Optional[str] = None
    created_at: Optional[datetime] = None
