import express from 'express';
import { createAddictionControllers, getAddictionControllers } from '../controllers/addictionControllers.js';

const router = express.Router();

router.get('/', getAddictionControllers)
router.post('/', createAddictionControllers)

export default router;