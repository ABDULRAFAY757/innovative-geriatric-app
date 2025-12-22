# Healthcare API

A comprehensive FastAPI-based Healthcare Management System with support for Patients, Doctors, Symptoms, and Medications.

## Features

- ✅ Async MongoDB integration using Motor
- ✅ RESTful API with proper error handling
- ✅ Comprehensive API documentation with Swagger UI
- ✅ Full CRUD operations for all entities
- ✅ Input validation using Pydantic models
- ✅ Health check endpoint

## Tech Stack

- **Framework**: FastAPI
- **Database**: MongoDB with Motor (async driver)
- **Async**: Python asyncio
- **Validation**: Pydantic
- **API Server**: Uvicorn

## Prerequisites

- Python 3.10+
- MongoDB Atlas account or local MongoDB instance
- Virtual environment (recommended)

## Installation

1. **Clone the repository**
   ```bash
   cd d:\Medical\backend
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure MongoDB**
   - Copy `.env.example` to `.env`
   - Update with your MongoDB credentials
   ```bash
   MONGO_URI=mongodb+srv://username:password@cluster.mongodb.net/healthcare_db?retryWrites=true&w=majority
   ```

## Running the Application

```bash
cd d:\Medical\backend
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: `http://127.0.0.1:8000`

## API Documentation

### Interactive Swagger UI
- **URL**: http://127.0.0.1:8000/docs
- Complete API documentation with try-it-out functionality

### Health Check
- **Endpoint**: `GET /health`
- **Purpose**: Verify API is running
- **Response**: `{"status": "healthy", "message": "API is running"}`

## API Endpoints

### Patients
- `POST /patients` - Create patient
- `GET /patients` - Get all patients
- `GET /patients/{id}` - Get patient by ID
- `PUT /patients/{id}` - Update patient
- `DELETE /patients/{id}` - Delete patient

### Doctors
- `POST /doctors` - Create doctor
- `GET /doctors` - Get all doctors
- `GET /doctors/{id}` - Get doctor by ID
- `PUT /doctors/{id}` - Update doctor
- `DELETE /doctors/{id}` - Delete doctor

### Symptoms
- `POST /symptoms` - Create symptom
- `GET /symptoms` - Get all symptoms
- `GET /symptoms/{id}` - Get symptom by ID
- `PUT /symptoms/{id}` - Update symptom
- `DELETE /symptoms/{id}` - Delete symptom

### Medications
- `POST /medications` - Create medication
- `GET /medications` - Get all medications
- `GET /medications/{id}` - Get medication by ID
- `PUT /medications/{id}` - Update medication
- `DELETE /medications/{id}` - Delete medication

## Project Structure

```
backend/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app and routes
│   ├── config.py         # Configuration management
│   ├── database.py       # MongoDB collections and utilities
│   ├── models.py         # Pydantic data models
│   └── crud.py           # CRUD helpers
├── .env                  # Environment variables (create from .env.example)
├── .env.example          # Example environment file
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Error Handling

All endpoints include proper error handling:
- **400 Bad Request**: Invalid ID format
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server errors (logged)

## Best Practices Implemented

✅ Async/await for non-blocking I/O  
✅ Proper error handling with HTTPException  
✅ Input validation with Pydantic  
✅ Environment variable management  
✅ Docstrings for all endpoints  
✅ Organized code structure with separation of concerns  
✅ Proper import statements and module organization  
✅ Type hints throughout the code  

## Development

### Running tests (when available)
```bash
pytest
```

### Linting and formatting
```bash
# Install dev dependencies
pip install black flake8 pytest

# Format code
black app/

# Check style
flake8 app/
```

## Troubleshooting

### MongoDB Connection Error
- Verify MongoDB credentials in `.env`
- Check if MongoDB Atlas cluster is running
- Ensure IP whitelist includes your machine

### Import Errors
- Ensure all packages are installed: `pip install -r requirements.txt`
- Virtual environment is activated
- Running from correct directory

### Port Already in Use
```bash
# Run on different port
uvicorn app.main:app --reload --port 8001
```

## License

Proprietary - Healthcare System

## Support

For issues or questions, check the API documentation at `/docs`
