import express from 'express';
import { setupRoutes } from './routes';
import { setupMiddlewares, notFound, errorHandler } from './middlewares';

const app = express();

// Setup basic middlewares (logger, JSON, etc.)
setupMiddlewares(app);

// Setup routes
setupRoutes(app);

// Register not-found handler and error handler after routes
app.use(notFound);
app.use(errorHandler as any);

// Simple root handler for browser
app.get('/', (_req, res) => {
	res.send('Medical App Prototype API — visit /api for endpoints');
});

export default app;