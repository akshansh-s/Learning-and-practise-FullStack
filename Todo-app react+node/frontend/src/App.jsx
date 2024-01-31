import { useState, useEffect } from 'react'
import './App.css'
import { CreateTodo } from './components/CreateTodo'
import { Todos } from './components/Todos'

function App() {
  const [todos, setTodos] = useState([])

  useEffect(() => {
    fetch("http://localhost:3000/todos")
    .then(async function(res){
      const json= await res.json();
      setTodos(json.todos);
    })
  }, [])
  return (
    <>
      <div><center>
        <h1>Todo App Using React, Express, Mongodb</h1>
        <CreateTodo></CreateTodo>
        <Todos todos={todos}></Todos>
      </center></div>
    </>
  )
}

export default App
