const express=require('express');
const app=express();
app.use(express.json());

let balance=0;
let transactions=[];

// app.get('/',(req,res)=>{
//     res.send("Hello world");
// });

app.get('/balance',(req,res=>{
    res.send("The current balance is-  ${balance}");
}));

app.get('/history',(req,res)=>{
    res.send("These are the transactions- ${JSON.stringify(transactions)}");
});



app.listen(3000,()=>{
    console.log("App is running on http://localhost:3000");
});