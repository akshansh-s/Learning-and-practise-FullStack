require('dotenv').config();
const mongoose = require('mongoose');
//const MONGO = process.env.MONGO;
console.log('MongoDB URI:', process.env.MONGO);
mongoose.connect(process.env.MONGO);

const todoSchema = mongoose.Schema({
    title: String,
    description: String,
    completed: Boolean
});

const todo = mongoose.model('todos',todoSchema);

module.exports={todo}
