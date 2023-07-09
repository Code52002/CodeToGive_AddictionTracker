import { comparePassword, hashPassword } from "../utils/authUtils.js";
import authModel from "../models/authModel.js";
import JWT from 'jsonwebtoken'

export const authRegisterController = async (req, res) => {
  try {
    const { username, email, password } = req.body;
    // Validations
    if (!email) {
      return res.send({ message: "Email is Required" });
    }
    if (!password) {
      return res.send({ message: "Password is Required" });
    }
    if (!username) {
      return res.send({ message: "Username is Required" });
    }
    // Check User
    const existingUser = await authModel.findOne({ email });
    // Existing User
    if (existingUser) {
      return res.status(200).end({
        success: false,
        message: "Already registered please login",
      });
    }
    // Resiter User
    const hashedPassword = await hashPassword(password);
    // Save
    const user = await new authModel({
      username,
      email,
      password: hashedPassword,
    }).save();
    res.status(201).send({
      success: true,
      message: "User Registered Successfully",
      user,
    });
  } catch (error) {
    console.log(`Register Controller Error: ${error}`);
    res.status(500).send({
      success: false,
      message: "Error in registration",
      error,
    });
  }
};

export const authLoginController = async (req, res) => {
  try {
    const { username, password } = req.body;
    // Validation
    if (!username || !password) {
      return res.status(404).send({
        success: false,
        message: "Invalid Email or Password",
      });
    }
    const user = await authModel.findOne({ username });
    if (!user) {
      return res.status(404).send({
        success: false,
        message: "Username is not registered",
      });
    }
    const match = await comparePassword(password, user.password);
    if (!match) {
      return res.status(200).send({
        success: false,
        message: "Invalid Password",
      });
    }
    // Token
    const token = await JWT.sign(
        { _id: user._id },
        process.env.JWT_SECRET_KEY,
        { expiresIn: "7d" }
      );
      res.status(200).send({
        success: true,
        message: "Login Successfull",
        user: {
          _id: user._id,
          username: user.username,
          email: user.email,
        },
        token,
      });
  } catch (error) {
    console.log(`Login Controller Error: ${error}`);
    res.status(500).send({
      success: false,
      message: "Error in Login",
      error,
    });
  }
};

export const authUpdateProfileController = async (req, res) => {
  res.status(200).send({ message: "Auth Update Profile is Working Fine" });
};

export const getAllUsers = async (req, res) => {
  try {
    const users = await authModel.find();
    res.status(200).send({ success: true, users });
  } catch (error) {
    console.log(`Get All Users Error: ${error}`);
    res.status(500).send({ success: false, message: "Error in getting users" });
  }
}