from fastapi import APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(
    prefix="/patients",
    tags=["patients"]
)

db = database.SessionLocal()

@router.get("/", response_model=list[schemas.Patient])
def get_patients():
    return db.query(models.Patient).all()
