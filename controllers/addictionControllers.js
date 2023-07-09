import Addiction from '../models/addictionModels.js';

export const createAddictionControllers = async (req, res) => {
    const { username, result } = req.body;
    try {
        const newAddiction = new Addiction({
            username,
            result
        });
        await newAddiction.save();
        res.status(201).json(newAddiction);
    } catch (error) {
        res.status(409).json({ message: error.message });
    }
}

export const getAddictionControllers = async (req, res) => {
    try {
        const addictions = await Addiction.find();
        res.status(200).json(addictions);
    } catch (error) {
        res.status(404).json({ message: error.message });
    }
}