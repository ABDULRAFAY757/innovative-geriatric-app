# My Express App

## Overview
This project is a simple Express application built with TypeScript. It serves as a template for creating RESTful APIs and can be easily extended with additional features.

## Features
- Modular structure with controllers, services, models, and middlewares.
- TypeScript support for type safety and better development experience.
- Example environment variables configuration.

## Getting Started

### Prerequisites
- Node.js (version 14 or higher)
- npm (Node package manager)

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd my-express-app
   ```
3. Install the dependencies:
   ```
   npm install
   ```

### Configuration
- Copy the `.env.example` file to `.env` and update the environment variables as needed.

### Running the Application
To start the application, run:
```
npm start
```
The server will start on the specified port (default is 3000).

### Directory Structure
- `src/`: Contains the source code of the application.
  - `app.ts`: Initializes the Express application.
  - `server.ts`: Starts the server.
  - `controllers/`: Contains controller classes for handling requests.
  - `routes/`: Sets up application routes.
  - `services/`: Contains business logic and data interaction.
  - `models/`: Defines data structures.
  - `middlewares/`: Contains middleware functions.
  - `utils/`: Provides utility functions.
  - `types/`: Defines TypeScript interfaces and types.

### License
This project is licensed under the MIT License. See the LICENSE file for details.