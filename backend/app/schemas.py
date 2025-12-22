from pydantic import BaseModel
from typing import List, Optional

class MedicationBase(BaseModel):
    name: str
    dosage: str
    frequency: str
    instructions: str

class MedicationCreate(MedicationBase):
    patient_id: int

class Medication(MedicationBase):
    id: int
    class Config:
        orm_mode = True

class PatientBase(BaseModel):
    user_id: int
    date_of_birth: str
    medical_history_summary: Optional[str]
    emergency_contact: Optional[str]

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int
    medications: List[Medication] = []
    class Config:
        orm_mode = True
