import express from 'express'
import { createCounselling, getAllCounselling, getSingleCounselling } from '../controllers/counsellingController.js'

const router = express.Router()

router.get('/', getAllCounselling)
router.post('/', createCounselling)
router.get('/:id', getSingleCounselling)

export default router