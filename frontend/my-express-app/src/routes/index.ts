
import { Router, Express } from 'express';
import { UserController } from '../controllers/index';

const router = Router();

const userCtrl = new UserController();

router.get('/some-route', userCtrl.getUsers.bind(userCtrl));
router.post('/another-route', userCtrl.createUser.bind(userCtrl));

export const setupRoutes = (app: Express) => {
    app.use('/api', router);
};

export default router;