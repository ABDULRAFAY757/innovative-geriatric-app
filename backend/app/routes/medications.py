from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter(
    prefix="/medications",
    tags=["medications"]
)

@router.post("/", response_model=schemas.Medication)
def create_medication(med: schemas.MedicationCreate, db: Session = Depends(database.get_db)):
    db_med = models.Medication(**med.dict())
    db.add(db_med)
    db.commit()
    db.refresh(db_med)
    return db_med

@router.get("/{patient_id}", response_model=List[schemas.Medication])
def read_medications(patient_id: int, db: Session = Depends(database.get_db)):
    return db.query(models.Medication).filter(models.Medication.patient_id == patient_id).all()

@router.post("/log", response_model=schemas.MedicationLog)
def log_medication(log: schemas.MedicationLogCreate, db: Session = Depends(database.get_db)):
    db_log = models.MedicationLog(**log.dict())
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log
