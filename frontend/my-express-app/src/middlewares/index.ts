import { Request, Response, NextFunction, Express } from 'express';

export const logger = (req: Request, res: Response, next: NextFunction) => {
    console.log(`${req.method} ${req.url}`);
    next();
};

export const errorHandler = (err: any, _req: Request, res: Response, _next: NextFunction) => {
    console.error(err.stack);
    res.status(500).send('Something broke!');
};

export const notFound = (_req: Request, res: Response, _next: NextFunction) => {
    res.status(404).send('Not Found');
};

// Setup function used by src/app.ts — only register basic middlewares (not error handlers)
export const setupMiddlewares = (app: Express) => {
    app.use(logger);
};