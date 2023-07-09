import mongoose from 'mongoose';

const userLocationSchema = new mongoose.Schema({
    userid: {
        type: String,
    },
    latitude: {
        type: Number,
    },
    longitude: {
        type: Number,
    },
    college: {
        type: String,
    }
})

export default mongoose.model('Location', userLocationSchema);