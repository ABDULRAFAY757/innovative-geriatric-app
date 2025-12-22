from fastapi import FastAPI
from .database import Base, engine
from .routes import patients, medications

app = FastAPI(title="Innovative Geriatrics API")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(patients.router)
app.include_router(medications.router)

@app.get("/")
def root():
    return {"message": "API running successfully"}
