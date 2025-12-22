# Frontend Setup Instructions

**Note**: Your system currently lacks Node.js, so the frontend code has been generated but not installed.

## Prerequisites
1.  **Install Node.js**: Download "LTS" version from [nodejs.org](https://nodejs.org/).
2.  **Verify Installation**: Open a terminal and run `node --version` and `npm --version`.

## How to Run the Frontend
Once Node is installed, follow these steps:

1.  Open Terminal in `frontend/` folder:
    ```powershell
    cd c:\Users\abdularafay\Desktop\Medical_App\frontend
    ```
2.  Install Dependencies:
    ```powershell
    npm install
    ```
3.  Start the Development Server:
    ```powershell
    npm run dev
    ```
4.  Open Browser:
    Go to `http://localhost:5173`

## Login Credentials (Mock)
-   **Patient**: `patient@test.com` (Any password)
-   **Family**: `family@test.com` (Any password)

## Features Included
-   **Dashboard**: Shows Vitals, Heart Rate, and Medication status.
-   **Medication List**: Interactive list (Mark as Taken / Not Taken).
-   **Marketplace**: Mock equipment request page.
-   **Fall Detection**: Simulation button.
