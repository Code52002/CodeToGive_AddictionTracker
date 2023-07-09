import express, { application } from "express";
import dotenv from "dotenv";
import cors from "cors";
import connectDB from "./db/db.js";
import authRouter from "./routes/authRoutes.js";
import counsellingRouter from "./routes/counsellingRoutes.js";
import userLocationRoutes from "./routes/userLocationRoutes.js";
import mlAlgoRoutes from './routes/mlAlgoRoutes.js'
import questionAnswerRoutes from './routes/questionAnswerRoutes.js'
import addictionRoutes from './routes/addictionRoutes.js'

dotenv.config();

connectDB();

const app = express();

app.use(cors());
app.use(express.json());
app.use("/api/auth", authRouter);
app.use("/api/counselling", counsellingRouter);
app.use("/api/location", userLocationRoutes);
app.use('/api/mlAlgo', mlAlgoRoutes);
app.use('/api/qna', questionAnswerRoutes);
app.use('/api/addiction', addictionRoutes);

const port = process.env.PORT || 8000;

app.use(cors());

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
