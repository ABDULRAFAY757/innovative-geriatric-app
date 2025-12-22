from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, database
from passlib.context import CryptContext

router = APIRouter(tags=["Authentication"])
pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

@router.post("/register", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(email=user.email, full_name=user.full_name, role=user.role, password_hash=hashed_password)
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        raise HTTPException(status_code=400, detail="Email already registered")

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    # Simple mock login for prototype
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not pwd_context.verify(user.password, db_user.password_hash):
        raise HTTPException(status_code=404, detail="Invalid credentials")
    return {"message": "Login successful", "user_id": db_user.id, "role": db_user.role, "access_token": "mock-token-123"}
