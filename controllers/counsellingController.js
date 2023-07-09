import counsellingModel from "../models/counsellingModel.js"
export const getAllCounselling = async (req, res) => {
  try {
    const counselling = await counsellingModel.find()
    res.status(200).json(counselling)
  } catch (error) {
    res.status(500).json({ message: error.message })
  }
}

export const createCounselling = async (req, res) => {
    try {
        const {user, name, email, location, college, age, number} = req.body
        const counselling = await counsellingModel.create({user, name, email, location, college, age, number})
        res.status(200).json({
            success: true,
            message: "Counselling created successfully",
            counselling
        })
    } catch (error) {
        res.status(500).json({ message: error.message })
    }
}

export const getSingleCounselling = async (req, res) => {
    try {
        const {user} = req.params
        const counselling = await counsellingModel.findById({user: user})
        res.status(200).json(counselling)
    } catch (error) {
        res.status(500).json({ message: error.message })
    }
}