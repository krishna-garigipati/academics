import React from "react";
function App(){
  const name = "Nagendrudu";
  const year = new Date().getFullYear();

  return(
    <div>
      <h1>Welcome, {name}</h1>
      <p>Current Year: {year}</p>
      <p>2+3 = {2+3}</p>
    </div>
  );
}

export default App; 