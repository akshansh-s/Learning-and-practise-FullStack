import { useState } from "react";

export function CreateTodo() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const addTodo = () => {
    fetch("http://localhost:3000/todo", {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        title: title,
        description: description
      })
    })
    .then(async function(res){
      const json = await res.json();
      alert("Todo added");
    })
  }

  return (
    <div>
      <input id="title" style={{ padding:10, margin:10 }} type="text" placeholder="title" onChange={e => setTitle(e.target.value)}></input><br></br>
      <input id="description" style={{ padding:10, margin:10 }} type="text" placeholder="description" onChange={e => setDescription(e.target.value)}></input><br></br>
      <button style={{ padding:10, margin:10 }} onClick={addTodo}>Add a todo</button>
    </div>
  )
}
