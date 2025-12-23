import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Add token to requests if available
api.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
});

export const medicationService = {
    getMedications: (patientId) => api.get(`/medications/${patientId}`),
    logMedication: (data) => api.post('/medications/log', data),
};

export const patientService = {
    getPatientProfile: (patientId) => api.get(`/patients/${patientId}`),
    getVitals: (patientId) => api.get(`/patients/${patientId}/vitals`), // Note: Need to verify if this route exists or we use getPatient
    addVital: (patientId, data) => api.post(`/patients/${patientId}/vitals`, data),
};

export default api;
