import mongoose from 'mongoose';

const counsellingSchema = new mongoose.Schema({
    user: {
        type: String,
        required: true,
    },
    name: {
        type: String,
        required: true,
    },
    email: {
        type: String,
        required: true,
    },
    location: {
        type: String,
        required: true,
    },
    college: {
        type: String,
        required: true,
    },
    age: {
        type: Number,
        required: true,
    },
    number: {
        type: Number,
        required: true,
    },
})

export default mongoose.model('Counselling', counsellingSchema);