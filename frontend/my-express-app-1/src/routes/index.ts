import { Router } from 'express';
import { SomeController } from '../controllers/index';

const router = Router();

router.get('/some-route', SomeController.someMethod);
router.post('/another-route', SomeController.anotherMethod);

export default (app) => {
    app.use('/api', router);
};