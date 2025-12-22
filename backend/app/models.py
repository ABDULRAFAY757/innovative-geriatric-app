from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String)
    password_hash = Column(String)   # store hashed password
    role = Column(String)  # PATIENT, FAMILY, DOCTOR
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    patients = relationship("Patient", back_populates="user")
    linked_patients = relationship("FamilyLink", back_populates="family_member")
    equipment_requests = relationship("EquipmentRequest", back_populates="requester")

class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date_of_birth = Column(String)
    medical_history_summary = Column(String)
    emergency_contact = Column(String)
    cognitive_score = Column(Integer, default=0) # Mock Data for PoC

    user = relationship("User", back_populates="patients")
    medications = relationship("Medication", back_populates="patient")
    vitals = relationship("Vital", back_populates="patient")
    family_links = relationship("FamilyLink", back_populates="patient")
    alerts = relationship("Alert", back_populates="patient")

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
    logs = relationship("MedicationLog", back_populates="medication")

class MedicationLog(Base):
    __tablename__ = "medication_logs"
    id = Column(Integer, primary_key=True, index=True)
    medication_id = Column(Integer, ForeignKey("medications.id"))
    taken_at = Column(DateTime, default=datetime.datetime.utcnow)
    status = Column(String) # TAKEN, MISSED, SKIPPED
    
    medication = relationship("Medication", back_populates="logs")

class Vital(Base):
    __tablename__ = "vitals"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    type = Column(String) # BP, HR, WEIGHT, GLUCOSE
    value = Column(String)
    recorded_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    patient = relationship("Patient", back_populates="vitals")

class FamilyLink(Base):
    __tablename__ = "family_links"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    family_member_id = Column(Integer, ForeignKey("users.id"))
    relationship_type = Column(String) # SON, DAUGHTER, WIFE, etc.
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    patient = relationship("Patient", back_populates="family_links")
    family_member = relationship("User", back_populates="linked_patients")

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    type = Column(String) # FALL, SOS, VITALS
    message = Column(String)
    status = Column(String, default="NEW") # NEW, READ, RESOLVED
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    patient = relationship("Patient", back_populates="alerts")

class EquipmentRequest(Base):
    __tablename__ = "equipment_requests"
    id = Column(Integer, primary_key=True, index=True)
    requester_id = Column(Integer, ForeignKey("users.id"))
    item_name = Column(String)
    description = Column(String)
    status = Column(String, default="OPEN") # OPEN, FULFILLED
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    requester = relationship("User", back_populates="equipment_requests")
