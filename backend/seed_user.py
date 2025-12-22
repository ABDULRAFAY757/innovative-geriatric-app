from app.database import SessionLocal, engine, Base
from app import models
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    # Check if user exists
    user = db.query(models.User).filter(models.User.email == "patient@test.com").first()
    if not user:
        print("Creating test user: patient@test.com / password123")
        hashed_pw = pwd_context.hash("password123")
        new_user = models.User(
            email="patient@test.com",
            full_name="Saeed Al-Ghamdi",
            role="PATIENT",
            password_hash=hashed_pw
        )
        db.add(new_user)
        db.commit()
    else:
        print("Test user already exists.")
    db.close()

if __name__ == "__main__":
    seed()
