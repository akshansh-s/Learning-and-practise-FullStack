

export function Todos({todos}){
    return <div>
        {todos.map(function(todo){
            return <div>
                <h2>{todo.title}</h2>
                <h3>{todo.description}</h3>
                <button>{todo.completed==true?"Completed": "Mark as complete"}</button>
            </div>
        })}
    </div>
}