import { useState } from "react";


export function CreateTodo(){

    const [title,setTitle]=useState("");
    const [description,setDescription]=useState("");

    return <div>
        <input id="title" style= {{
            padding:10,
            margin:10
        }} type="text" placeholder="title"></input><br></br>
        <input id="description" style= {{
            padding:10,
            margin:10
        }} type="text" placeholder="description"></input><br></br>

        <button style= {{
            padding:10,
            margin:10
        }} onClick={()=>{
            fetch("http://localhost:3000/todos"), {
                method: "POST",
                body: {
                    title: title,
                    description: description
                }
            }
            .then(async function(res){
                const json = await res.json();
                alert("Todo added");
            })
        }}>Add a todo</button>
    </div>
}