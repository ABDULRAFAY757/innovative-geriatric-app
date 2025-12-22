from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter(
    prefix="/patients",
    tags=["patients"]
)

@router.post("/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, user_id: int, db: Session = Depends(database.get_db)):
    # Ensure user exists first
    db_patient = models.Patient(**patient.dict(), user_id=user_id)
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@router.get("/", response_model=List[schemas.Patient])
def get_patients(db: Session = Depends(database.get_db)):
    return db.query(models.Patient).all()

@router.get("/{patient_id}", response_model=schemas.Patient)
def get_patient(patient_id: int, db: Session = Depends(database.get_db)):
    patient = db.query(models.Patient).filter(models.Patient.id == patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.post("/{patient_id}/vitals", response_model=schemas.Vital)
def add_vital(patient_id: int, vital: schemas.VitalBase, db: Session = Depends(database.get_db)):
    db_vital = models.Vital(**vital.dict(), patient_id=patient_id)
    db.add(db_vital)
    db.commit()
    db.refresh(db_vital)
    return db_vital
