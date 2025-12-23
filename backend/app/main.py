from fastapi import FastAPI, HTTPException
from app.database import patient_collection, doctor_collection
from app.crud import serialize
from app.models import Patient, Doctor
from bson import ObjectId
from app.database import medication_collection, symptom_collection
from app.models import Medication, Symptom


app = FastAPI(title="Healthcare API")

@app.get("/")
async def root():
    return {"message": "Healthcare API is running!"}

# ---------------- PATIENT CRUD ----------------
@app.post("/patients", response_model=Patient)
async def create_patient(patient: Patient):
    result = await patient_collection.insert_one(patient.dict(exclude={"id"}))
    patient.id = str(result.inserted_id)
    return patient

@app.get("/patients")
async def get_patients():
    patients = []
    async for p in patient_collection.find():
        patients.append(serialize(p))
    return patients

@app.get("/patients/{id}")
async def get_patient(id: str):
    patient = await patient_collection.find_one({"_id": ObjectId(id)})
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return serialize(patient)

@app.put("/patients/{id}")
async def update_patient(id: str, patient: Patient):
    await patient_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": patient.dict(exclude={"id"})}
    )
    return {"message": "Patient updated"}

@app.delete("/patients/{id}")
async def delete_patient(id: str):
    await patient_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Patient deleted"}

# ---------------- DOCTOR CRUD ----------------
@app.post("/doctors", response_model=Doctor)
async def create_doctor(doctor: Doctor):
    result = await doctor_collection.insert_one(doctor.dict(exclude={"id"}))
    doctor.id = str(result.inserted_id)
    return doctor

@app.get("/doctors")
async def get_doctors():
    doctors = []
    async for d in doctor_collection.find():
        doctors.append(serialize(d))
    return doctors

@app.get("/doctors/{id}")
async def get_doctor(id: str):
    doctor = await doctor_collection.find_one({"_id": ObjectId(id)})
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return serialize(doctor)

@app.put("/doctors/{id}")
async def update_doctor(id: str, doctor: Doctor):
    await doctor_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": doctor.dict(exclude={"id"})}
    )
    return {"message": "Doctor updated"}

@app.delete("/doctors/{id}")
async def delete_doctor(id: str):
    await doctor_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Doctor deleted"}


# ---------------- MEDICATIONS ----------------
# ---------------- SYMPTOMS ----------------
@app.post("/symptoms")
async def create_symptoms(symptoms: list[Symptom]):
    inserted = []
    for s in symptoms:
        result = await symptom_collection.insert_one(s.dict(exclude={"id"}))
        inserted.append({"id": str(result.inserted_id), "symptom": s.symptom})
    return inserted

@app.get("/symptoms")
async def get_symptoms():
    symptoms = []
    async for s in symptom_collection.find():
        symptoms.append(serialize(s))
    return symptoms

@app.get("/symptoms/{id}")
async def get_symptom(id: str):
    symptom = await symptom_collection.find_one({"_id": ObjectId(id)})
    if not symptom:
        raise HTTPException(status_code=404, detail="Symptom not found")
    return serialize(symptom)

# ---------------- MEDICATIONS ----------------
@app.post("/medications")
async def create_medications(medications: list[Medication]):
    inserted = []
    for m in medications:
        result = await medication_collection.insert_one(m.dict(exclude={"id"}))
        inserted.append({"id": str(result.inserted_id), "name": m.name})
    return inserted

@app.get("/medications")
async def get_medications():
    meds = []
    async for m in medication_collection.find():
        meds.append(serialize(m))
    return meds

@app.get("/medications/{id}")
async def get_medication(id: str):
    med = await medication_collection.find_one({"_id": ObjectId(id)})
    if not med:
        raise HTTPException(status_code=404, detail="Medication not found")
    return serialize(med)