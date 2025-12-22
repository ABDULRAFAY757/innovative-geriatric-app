from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routes import patients, medications, auth, marketplace, alerts

app = FastAPI(title="Innovative Geriatrics API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173"], # React/Vite default ports
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(medications.router)
app.include_router(marketplace.router)
app.include_router(alerts.router)

@app.get("/")
def root():
    return {"message": "API running successfully"}
