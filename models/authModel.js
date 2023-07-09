import mongoose from "mongoose";

const userSchema = new mongoose.Schema({
  username: {
    type: String,
    required: true,
  },
  email: {
    type: String,
    required: true,
    unique: true,
  },
  password: {
    type: String,
    required: true,
  },
  // location: {
  //   type: String,
  //   default: "",
  // },
  // college: {
  //   type: String,
  //   default: "",
  // },
});

export default mongoose.model("User", userSchema);
