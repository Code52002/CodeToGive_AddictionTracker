import express from 'express';
import { authLoginController, authRegisterController, authUpdateProfileController, getAllUsers } from '../controllers/authControllers.js';
const router = express.Router();

router.post('/register', authRegisterController)
router.post('/login', authLoginController)
router.get('/users', getAllUsers)
router.put('/update-profile', authUpdateProfileController) // Not required

export default router