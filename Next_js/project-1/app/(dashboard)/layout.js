import NewTodo from "@/components/NewTodoForm";

function DashboardLayout({children}){

    return(
        <div>
            <h1>Dashboard</h1>

            <div>
                <NewTodo/>
            </div>

            <div>{children}</div>
        </div>
    )

}

export default DashboardLayout;