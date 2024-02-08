import { useEffect, useState } from 'react'
import axios from "axios";
import './App.css'

function App() {
  const [todos, setTodos] = useState([]);

  useEffect(()=>{
    axios.get("https://sum-server.100xdevs.com/todos")
      .then(function(response){
        setTodos(response.data.todos)
      })
  }, []);
  return (
    <>
      {todos.map(todo=> <Todo title={todo.title} description= {todo.description} />)}
    </>
  )
}

function Todo({title, description}){
  return (
    <>
      <center>
      <h2>{title}</h2>
      <h4>{description}</h4>
      </center>
    </>
  )
}

export default App
