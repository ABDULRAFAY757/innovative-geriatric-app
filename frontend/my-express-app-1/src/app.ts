import express from 'express';
import { setupRoutes } from './routes';
import { setupMiddlewares } from './middlewares';

const app = express();

// Setup middlewares
setupMiddlewares(app);

// Setup routes
setupRoutes(app);

export default app;