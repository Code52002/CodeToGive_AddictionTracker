import QuestionAnswerModel from '../models/qnaModels.js'

export const getQuestionAnswer = async (req, res) => {
    const questionAnswer = await QuestionAnswerModel.find({})
    res.status(200).send({success: true, questionAnswer, message: "Fetched Successfully"})
}

export const createQuestionAnswer = async (req, res) => {
    try {
        const {username, answers} = req.body
        const createdQNA = await QuestionAnswerModel.create({username, answers})
        res.send({success: true, createdQNA, message: "Created Successfully"})
    } catch (error) {
        
    }
}