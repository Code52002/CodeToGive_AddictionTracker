import mongoose from 'mongoose';

const qnaSchema = new mongoose.Schema({
    username: {
        type: String,
    },
    answers: {
        type: Array,
    }
})

export default mongoose.model('Qna', qnaSchema);