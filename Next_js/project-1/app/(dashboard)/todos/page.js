import TodoList from "@/components/TodoList";


function helloPage(){

    const todos = [{_id : 1 ,content : "does coding" }, {_id : 2 ,content : 'excersice'} , {_id : 3 ,content : "namaz"} , {_id : 4 ,content : "talawat"},]
    return(
        <>
        <div>Todes Page</div>
        <TodoList todos = {todos}/>
        </>
        
    )
}

export default helloPage;