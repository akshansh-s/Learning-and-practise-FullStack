import { useEffect, useState } from 'react'
import axios from "axios";
import './App.css'

function App() {
  return <div>
    <Todo id={3}/>
  </div>
  
}

function Todo({id}) {
  const [todo, setTodo] = useState({});

  useEffect(()=>{
    axios.get("https://sum-server.100xdevs.com/todo?id="+id)
      .then(response=>{
        setTodo(response.data.todo)
      })
  }, []);
  // return (
  //   <>
  //     {todos.map(todo=> <Todo title={todo.title} description= {todo.description} />)}
  //   </>
  //)
  return (
    <>
      <center>
      <h2>{todo.title}</h2>
      <h4>{todo.description}</h4>
      </center>
    </>
  )
}

export default App
