import express from "express";
import { spawn } from "child_process";
// const { spawn } = require('child_process');
const router = express.Router();

router.post("/", async (req, res) => {
  let { type, data } = req.body;
  console.log('====================================');
  console.log(type, data);
  console.log('====================================');
  const jsonString = JSON.stringify({ type, data });
  const pythonProcess = spawn("python", ["./MlData/merging.py", jsonString]);
  // console.log(2);
  pythonProcess.stdout.on("data", (data) => {
    console.log(`Python script output: ${data}`);
    res.send({message: data.toString()})
  });

  // Handle Python process errors
  pythonProcess.on("error", (error) => {
    console.error(`Error executing Python script: ${error}`);
  });
});

export default router;
