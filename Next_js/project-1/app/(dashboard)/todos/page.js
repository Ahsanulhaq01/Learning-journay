import TodoList from "@/components/TodoList";
import db from "@/utils/db.js"
const getData = async()=>{
        const todos = await db.todo.find({})
        return todos;
    }


async function helloPage(){

    const todos = await getData()
    return(
        <>
        <div>Todes Page</div>
        <TodoList todo = {todos}/>
        </>
        
    )
}

export default helloPage;