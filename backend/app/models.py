from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from enum import Enum

from typing import Optional, List


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

# ---------------- Symptoms ----------------
class Symptom(BaseModel):
    id: Optional[str] = None
    symptom: str

# ---------------- Medications ----------------
class Medication(BaseModel):
    id: Optional[str] = None
    name: str  # treatment or medicine name
