import UserLocationInfo from '../models/userLocationInfo.js';
export const createUserLocationInfo = async (req, res) => {
    const { userid, latitude, longitude, college } = req.body;
    try {
        const userLocationData = await UserLocationInfo.create({
            userid,
            latitude,
            longitude,
            college
        })
        res.status(201).json({ success: true, userLocationData })
    } catch (error) {
        res.status(500).json({ error })
    }
}

export const getUserLocationInfo = async (req, res) => {
    try {
        const userLocationData = await UserLocationInfo.find()
        res.status(200).json({ userLocationData })
    } catch (error) {
        console.log(error)
        res.status(500).json({ error })
    }
}