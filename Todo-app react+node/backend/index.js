const express= require('express');
const { createTodo } = require('./types');
const app =express();
const port=3000;


app.use(express.json());


app.post('/todo', (req,res)=>{
    const createPayload=req.body;
    const parsedPayload=createTodo.safeParse(createPayload);
    if(!parsedPayload.success){
        res.status(411).json({
            msg:"You sent the wrong inputs"
        })
        return;
    }
})

app.get('/todos', (req,res)=>{
    
})

app.put('/completed', (req,res)=>{
    const updatePayload=req.body;
    const parsedPayload=createTodo.safeParse(updatePayload);
    if(!parsedPayload.success){
        res.status(411).json({
            msg:"You sent the wrong inputs"
        })
        return;
    }
})

app.listen(port,()=>{
    console.log(`App is running on port- ${3000}`)
});