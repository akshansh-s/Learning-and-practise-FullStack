require('dotenv').config();

const mongoose = require('mongoose');

// Use the environment variable
mongoose.connect(process.env.MONGODB_URI);

const todoSchema = mongoose.Schema({
    title: String,
    description: String,
    completed: Boolean
});

