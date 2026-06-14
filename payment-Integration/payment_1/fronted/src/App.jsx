import './App.css'

function App() {
  const amount = 1000;
  function handleclick(){
    console.log("hello from fronted")
  }

  return (
    <>
      <button onClick={handleclick}>click to apy amount</button>
    </>
  )
}

export default App
