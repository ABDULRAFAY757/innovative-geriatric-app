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
        user = models.User(
            email="patient@test.com",
            full_name="Saeed Al-Ghamdi",
            role="PATIENT",
            password_hash=hashed_pw
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    # Create Patient Profile
    patient = db.query(models.Patient).filter(models.Patient.user_id == user.id).first()
    if not patient:
        print("Creating Patient Profile for Saeed...")
        patient = models.Patient(
            user_id=user.id,
            date_of_birth="1950-01-01",
            medical_history_summary="Type 2 Diabetes, Hypertension",
            emergency_contact="Ahmed Al-Ghamdi: +966 50 123 4567",
            cognitive_score=85
        )
        db.add(patient)
        db.commit()
        db.refresh(patient)

    # Add Medications if empty
    if not db.query(models.Medication).filter(models.Medication.patient_id == patient.id).first():
        print("Adding initial medications...")
        meds = [
            models.Medication(patient_id=patient.id, name="Aspirin", dosage="100mg", frequency="Daily", instructions="Take after breakfast", start_date="2024-01-01"),
            models.Medication(patient_id=patient.id, name="Metformin", dosage="500mg", frequency="Daily", instructions="Twice a day with meals", start_date="2024-01-01"),
            models.Medication(patient_id=patient.id, name="Lisinopril", dosage="10mg", frequency="Daily", instructions="Before bed", start_date="2024-01-01")
        ]
        db.add_all(meds)
    
    # Add Vitals if empty
    if not db.query(models.Vital).filter(models.Vital.patient_id == patient.id).first():
        print("Adding initial vitals...")
        vitals = [
            models.Vital(patient_id=patient.id, type="HR", value="72"),
            models.Vital(patient_id=patient.id, type="BP", value="120/80"),
            models.Vital(patient_id=patient.id, type="WEIGHT", value="78kg")
        ]
        db.add_all(vitals)

    db.commit()
    print("Seeding completed successfully.")
    db.close()

if __name__ == "__main__":
    seed()
