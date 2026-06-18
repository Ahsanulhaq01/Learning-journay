import Todo from "./Todo"
function TodoList({todos}){

     return(
        <div>

            {
                todos?.map((todo)=>{
                return  <Todo todo={todo.content} key={todo._id}/>
                })
            }
        </div>
     )
}

export default TodoList