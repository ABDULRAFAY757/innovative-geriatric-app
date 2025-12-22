from fastapi import APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas, database

router = APIRouter(
    prefix="/medications",
    tags=["medications"]
)

db = database.SessionLocal()

@router.get("/", response_model=list[schemas.Medication])
def get_medications():
    return db.query(models.Medication).all()
