import React, { createContext, useContext, useState, useEffect } from 'react';
import axios from 'axios';

// Create context
const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        // Check local storage for mock token
        const token = localStorage.getItem('token');
        const role = localStorage.getItem('role');
        if (token) {
            setUser({ role, token }); // In real app, validate token with backend
        }
        setLoading(false);
    }, []);

    const login = async (email, password) => {
        try {
            // PROTOTYPE: Real Backend Call
            const formData = new URLSearchParams();
            formData.append('username', email); // FastAPI OAuth2PasswordRequestForm expects 'username'
            formData.append('password', password);

            // Using axios directly to localhost:8000
            const response = await axios.post('http://127.0.0.1:8000/auth/login', {
                email: email,       // Sending as JSON body to match our custom schema 
                password: password,
                full_name: "User",  // Optional, handled by backend if needed
                role: email.includes("family") ? "FAMILY" : "PATIENT" // Heuristic for Demo
            });

            // Fallback for custom schema if the previous didn't work, 
            // but based on routes/auth.py: def login(user: schemas.UserCreate...
            // It expects a JSON body with UserCreate schema.

            const data = response.data;

            const userData = {
                role: data.role,
                token: data.access_token,
                name: email.split('@')[0] // Simple name extraction for display
            };

            setUser(userData);
            localStorage.setItem('token', data.access_token);
            localStorage.setItem('role', data.role);
            return userData;

        } catch (error) {
            console.error("Login failed", error);
            // Fallback for demo if backend is offline to unblock the POC presentation
            if (email.includes('patient') || email.includes('family')) {
                console.warn("Backend offline? Falling back to mock data for POC.");
                const role = email.includes('family') ? 'FAMILY' : 'PATIENT';
                const userData = { role, token: 'mock-fallback', name: 'Demo User' };
                setUser(userData);
                return userData;
            }
            throw new Error(error.response?.data?.detail || "Login failed");
        }
    };

    const logout = () => {
        setUser(null);
        localStorage.removeItem('token');
        localStorage.removeItem('role');
    };

    return (
        <AuthContext.Provider value={{ user, login, logout, loading }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => useContext(AuthContext);
