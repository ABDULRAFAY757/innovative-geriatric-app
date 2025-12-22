from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# --- Medication Schemas ---
class MedicationBase(BaseModel):
    name: str
    dosage: str
    frequency: str
    instructions: str
    start_date: Optional[str] = None
    end_date: Optional[str] = None

class MedicationCreate(MedicationBase):
    patient_id: int

class Medication(MedicationBase):
    id: int
    patient_id: int
    class Config:
        orm_mode = True

# --- Medication Log Schemas ---
class MedicationLogBase(BaseModel):
    status: str
    taken_at: Optional[datetime] = None

class MedicationLogCreate(MedicationLogBase):
    medication_id: int

class MedicationLog(MedicationLogBase):
    id: int
    medication_id: int
    class Config:
        orm_mode = True

# --- Vital Schemas ---
class VitalBase(BaseModel):
    type: str
    value: str

class VitalCreate(VitalBase):
    patient_id: int

class Vital(VitalBase):
    id: int
    recording_at: Optional[datetime] = None
    class Config:
        orm_mode = True

# --- Alert Schemas ---
class AlertBase(BaseModel):
    type: str # FALL, SOS
    message: str
    status: str = "NEW"

class AlertCreate(AlertBase):
    patient_id: int

class Alert(AlertBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

# --- Equipment Request Schemas ---
class EquipmentRequestBase(BaseModel):
    item_name: str
    description: str

class EquipmentRequestCreate(EquipmentRequestBase):
    pass

class EquipmentRequest(EquipmentRequestBase):
    id: int
    requester_id: int
    status: str
    created_at: datetime
    class Config:
        orm_mode = True

# --- Patient & User Schemas ---
class PatientBase(BaseModel):
    date_of_birth: str
    medical_history_summary: Optional[str]
    emergency_contact: Optional[str]
    cognitive_score: Optional[int] = 0

class PatientCreate(PatientBase):
    pass # user_id will be handled in backend logic or passed if admin

class Patient(PatientBase):
    id: int
    user_id: int
    medications: List[Medication] = []
    vitals: List[Vital] = []
    alerts: List[Alert] = []
    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str
    full_name: str
    role: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    patients: List[Patient] = [] # If user is a doctor or admin, might have many. If patient, just one.
    class Config:
        orm_mode = True
