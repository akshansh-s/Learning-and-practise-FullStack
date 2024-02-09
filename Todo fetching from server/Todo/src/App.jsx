import { useEffect, useState } from 'react'
import axios from "axios";
import './App.css'

function App() {
  const [idi, setIdi] = useState(1);
  return <div>
    <button onClick={function (){
      setIdi(1);
    }}>1</button>
    <button onClick={function (){
      setIdi(2);
    }}>2</button>
    <button onClick={() => setIdi(3)}>3</button>
    <button onClick={() => setIdi(4)}>4</button>
    <button onClick={() => setIdi(5)}>5</button>

    <Todo id={idi}/>
  </div>
  
}

function Todo({id}) {
  const [todo, setTodo] = useState({});

  useEffect(()=>{
    axios.get("https://sum-server.100xdevs.com/todo?id="+id)
      .then(response=>{
        setTodo(response.data.todo)
      })
  }, [id]);
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
