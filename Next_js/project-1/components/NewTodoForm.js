'use client'
import { useState } from "react";

function NewTodo() {
    const [newTodo, setNewTodo] = useState();

    console.log(window.localStorage)

    return (
        <>
            <form>
                <input type="text"></input>
            </form>
        </>
    )
}

export default NewTodo;