import express from 'express';
import { createUserLocationInfo, getUserLocationInfo } from '../controllers/userLocationControllers.js';

const router = express.Router();

router.post('/registerlocation', createUserLocationInfo)
router.get('/getlocation', getUserLocationInfo)

export default router;