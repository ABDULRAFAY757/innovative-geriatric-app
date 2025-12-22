<<<<<<< Updated upstream
from fastapi import FastAPI
from .database import Base, engine
from .routes import patients, medications

app = FastAPI(title="Innovative Geriatrics API")
=======
from fastapi import FastAPI, HTTPException
from app.database import patient_collection, doctor_collection, symptom_collection, medication_collection
from app.models import Patient, Doctor, Symptom, Medication
from app.crud import serialize
from bson import ObjectId
from bson.errors import InvalidId

app = FastAPI(
    title="Healthcare API",
    description="Complete Healthcare Management System with Patients, Doctors, Symptoms, and Medications",
    version="1.0.0"
)

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    await patient_collection.database.command("ping")
    return {"status": "MongoDB connected"}

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information"""
    return {
        "name": "Healthcare API",
        "version": "1.0.0",
        "documentation": "/docs"
    }
>>>>>>> Stashed changes

# Create database tables
Base.metadata.create_all(bind=engine)

<<<<<<< Updated upstream
# Include routes
app.include_router(patients.router)
app.include_router(medications.router)

@app.get("/")
def root():
    return {"message": "API running successfully"}
=======
@app.post("/patients", response_model=Patient, tags=["Patients"])
async def create_patient(patient: Patient):
    """Create a new patient"""
    result = await patient_collection.insert_one(patient.dict(exclude={"id"}))
    patient.id = str(result.inserted_id)
    return patient

@app.get("/patients", tags=["Patients"])
async def get_patients():
    """Get all patients"""
    patients = []
    async for p in patient_collection.find():
        patients.append(serialize(p))
    return patients

@app.get("/patients/{id}", response_model=Patient, tags=["Patients"])
async def get_patient(id: str):
    """Get a patient by ID"""
    try:
        patient = await patient_collection.find_one({"_id": ObjectId(id)})
        if not patient:
            raise HTTPException(status_code=404, detail="Patient not found")
        return serialize(patient)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid patient ID format")

@app.put("/patients/{id}", tags=["Patients"])
async def update_patient(id: str, patient: Patient):
    """Update a patient's information"""
    try:
        await patient_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": patient.dict(exclude={"id"})}
        )
        return {"message": "Patient updated successfully"}
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid patient ID format")

@app.delete("/patients/{id}", tags=["Patients"])
async def delete_patient(id: str):
    """Delete a patient"""
    try:
        await patient_collection.delete_one({"_id": ObjectId(id)})
        return {"message": "Patient deleted successfully"}
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid patient ID format")

# ---------------- DOCTOR CRUD ----------------

@app.post("/doctors", response_model=Doctor, tags=["Doctors"])
async def create_doctor(doctor: Doctor):
    """Create a new doctor"""
    result = await doctor_collection.insert_one(doctor.dict(exclude={"id"}))
    doctor.id = str(result.inserted_id)
    return doctor

@app.get("/doctors", tags=["Doctors"])
async def get_doctors():
    """Get all doctors"""
    doctors = []
    async for d in doctor_collection.find():
        doctors.append(serialize(d))
    return doctors

@app.get("/doctors/{id}", response_model=Doctor, tags=["Doctors"])
async def get_doctor(id: str):
    """Get a doctor by ID"""
    try:
        doctor = await doctor_collection.find_one({"_id": ObjectId(id)})
        if not doctor:
            raise HTTPException(status_code=404, detail="Doctor not found")
        return serialize(doctor)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid doctor ID format")

@app.put("/doctors/{id}", tags=["Doctors"])
async def update_doctor(id: str, doctor: Doctor):
    """Update a doctor's information"""
    try:
        await doctor_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": doctor.dict(exclude={"id"})}
        )
        return {"message": "Doctor updated successfully"}
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid doctor ID format")

@app.delete("/doctors/{id}", tags=["Doctors"])
async def delete_doctor(id: str):
    """Delete a doctor"""
    try:
        await doctor_collection.delete_one({"_id": ObjectId(id)})
        return {"message": "Doctor deleted successfully"}
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid doctor ID format")

# ---------------- SYMPTOMS CRUD ----------------

@app.post("/symptoms", response_model=Symptom, tags=["Symptoms"])
async def create_symptom(symptom: Symptom):
    """Create a new symptom"""
    result = await symptom_collection.insert_one(symptom.dict(exclude={"id"}))
    symptom.id = str(result.inserted_id)
    return symptom

@app.get("/symptoms", tags=["Symptoms"])
async def get_symptoms():
    """Get all symptoms"""
    symptoms = []
    async for s in symptom_collection.find():
        symptoms.append(serialize(s))
    return symptoms

@app.get("/symptoms/{id}", response_model=Symptom, tags=["Symptoms"])
async def get_symptom(id: str):
    """Get a symptom by ID"""
    try:
        symptom = await symptom_collection.find_one({"_id": ObjectId(id)})
        if not symptom:
            raise HTTPException(status_code=404, detail="Symptom not found")
        return serialize(symptom)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid symptom ID format")

@app.put("/symptoms/{id}", tags=["Symptoms"])
async def update_symptom(id: str, symptom: Symptom):
    """Update a symptom's information"""
    try:
        await symptom_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": symptom.dict(exclude={"id"})}
        )
        return {"message": "Symptom updated successfully"}
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid symptom ID format")

@app.delete("/symptoms/{id}", tags=["Symptoms"])
async def delete_symptom(id: str):
    """Delete a symptom"""
    try:
        await symptom_collection.delete_one({"_id": ObjectId(id)})
        return {"message": "Symptom deleted successfully"}
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid symptom ID format")

# ---------------- MEDICATIONS CRUD ----------------

@app.post("/medications", response_model=Medication, tags=["Medications"])
async def create_medication(medication: Medication):
    """Create a new medication"""
    result = await medication_collection.insert_one(medication.dict(exclude={"id"}))
    medication.id = str(result.inserted_id)
    return medication

@app.get("/medications", tags=["Medications"])
async def get_medications():
    """Get all medications"""
    medications = []
    async for m in medication_collection.find():
        medications.append(serialize(m))
    return medications

@app.get("/medications/{id}", response_model=Medication, tags=["Medications"])
async def get_medication(id: str):
    """Get a medication by ID"""
    try:
        medication = await medication_collection.find_one({"_id": ObjectId(id)})
        if not medication:
            raise HTTPException(status_code=404, detail="Medication not found")
        return serialize(medication)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid medication ID format")

@app.put("/medications/{id}", tags=["Medications"])
async def update_medication(id: str, medication: Medication):
    """Update a medication's information"""
    try:
        await medication_collection.update_one(
            {"_id": ObjectId(id)},
            {"$set": medication.dict(exclude={"id"})}
        )
        return {"message": "Medication updated successfully"}
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid medication ID format")

@app.delete("/medications/{id}", tags=["Medications"])
async def delete_medication(id: str):
    """Delete a medication"""
    try:
        await medication_collection.delete_one({"_id": ObjectId(id)})
        return {"message": "Medication deleted successfully"}
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid medication ID format")
>>>>>>> Stashed changes
