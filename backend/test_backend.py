import requests
import json
import time

BASE_URL = "http://127.0.0.1:8001"

def test_root():
    try:
        r = requests.get(f"{BASE_URL}/")
        print(f"ROOT: {r.status_code} - {r.json()}")
    except Exception as e:
        print(f"ROOT FAILED: {e}")

def test_auth_and_flow():
    # 1. Register Patient
    email = f"patient_{int(time.time())}@test.com"
    user_data = {
        "email": email,
        "full_name": "Test Patient",
        "role": "PATIENT",
        "password": "password123"
    }
    
    print("\n--- Registering User ---")
    try:
        r = requests.post(f"{BASE_URL}/register", json=user_data)
        print(f"REGISTER: {r.status_code}")
        if r.status_code != 200:
            print(r.text)
            return
        
        user_id = r.json()['id']
        print(f"Created User ID: {user_id}")
        
        # 2. Login
        print("\n--- Logging In ---")
        login_data = {"email": email, "password": "password123", "full_name": "Test Patient", "role": "PATIENT"}
        r = requests.post(f"{BASE_URL}/login", json=login_data)
        print(f"LOGIN: {r.status_code}")
        token = r.json().get('access_token')
        
        # 3. Create Patient Profile
        print("\n--- Creating Patient Profile ---")
        patient_data = {
            "date_of_birth": "1950-01-01",
            "medical_history_summary": "Hypertension",
            "emergency_contact": "911"
        }
        r = requests.post(f"{BASE_URL}/patients/?user_id={user_id}", json=patient_data)
        print(f"CREATE PATIENT: {r.status_code}")
        if r.status_code == 200:
            patient_id = r.json()['id']
            print(f"Patient ID: {patient_id}")
            
            # 4. Add Medication
            print("\n--- Adding Medication ---")
            med_data = {
                "name": "Panadol",
                "dosage": "500mg",
                "frequency": "Daily",
                "instructions": "After food",
                "patient_id": patient_id
            }
            r = requests.post(f"{BASE_URL}/medications/", json=med_data)
            print(f"ADD MED: {r.status_code}")

    except Exception as e:
        print(f"FLOW FAILED: {e}")

if __name__ == "__main__":
    print("Checking Backend Health...")
    test_root()
    test_auth_and_flow()
