import mongoose from "mongoose";

const addictionSchema = new mongoose.Schema({
  username: {
    type: String,
    required: true,
  },
  result: {
    type: String,
    required: true,
  },
});

export default mongoose.model("Addiction", addictionSchema);
