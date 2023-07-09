import express from 'express'
import { getQuestionAnswer, createQuestionAnswer } from '../controllers/questionAnswerControllers.js'

const router = express.Router()

router.get('/getquestionanswer', getQuestionAnswer)
router.post('/createquestionanswer', createQuestionAnswer)

export default router