//require('dotenv').config();
const mongoose = require('mongoose');
//console.log('MongoDB URI:', process.env.MONGO);
mongoose.connect('mongodb+srv://admin:Mongodb%402205@cluster0.kxjojk9.mongodb.net/todos');

const todoSchema = mongoose.Schema({
    title: String,
    description: String,
    completed: Boolean
});

const todo = mongoose.model('todos',todoSchema);

module.exports={todo}