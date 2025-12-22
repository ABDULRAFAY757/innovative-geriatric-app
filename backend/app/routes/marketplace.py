from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas, database

router = APIRouter(
    prefix="/marketplace",
    tags=["marketplace"]
)

@router.post("/request", response_model=schemas.EquipmentRequest)
def create_request(request: schemas.EquipmentRequestCreate, requester_id: int, db: Session = Depends(database.get_db)):
    db_req = models.EquipmentRequest(**request.dict(), requester_id=requester_id)
    db.add(db_req)
    db.commit()
    db.refresh(db_req)
    return db_req

@router.get("/", response_model=List[schemas.EquipmentRequest])
def get_requests(db: Session = Depends(database.get_db)):
    return db.query(models.EquipmentRequest).all()
