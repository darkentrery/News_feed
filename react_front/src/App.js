// import './App.css';
import MenuComponent from "./MenuComponent";
import './feed.css';
import {Link, Route, BrowserRouter as Router, Routes} from "react-router-dom";
import HomeComponent from "./HomeComponent";
import React, {useState} from "react";
import DetailComponent from "./DetailComponent";
import CreateComponent from "./CreateComponent";



function App() {
    console.log("hello")
    console.log(window.location)
    const [pk, setPk] = useState(window.location.search?.split('=')[1] || 1);
    let updatePk = (value) => setPk(value)
    console.log(pk)


  return (
    <div className="App">
      <header className="App-header">
        <Router>
        <div>
            <MenuComponent/>

            <main>
                <div className="features">
                    <Routes>
                        {/*<Route exact path={`/home/page=${page}`} element={<HomeComponent page={page} updatePk={updatePk} updatePage={updatePage}/>}/>*/}
                        <Route exact path={`/home`} element={<HomeComponent updatePk={updatePk}/>}/>
                        <Route exact path={`/`} element={<DetailComponent pk={pk}/>}/>
                        <Route exact path={`/Create`} element={<CreateComponent/>}/>



                    </Routes>
                </div>


            </main>

        </div>



        </Router>


        {/*<img src={logo} className="App-logo" alt="logo" />*/}

        <a className="App-link" href="https://reactjs.org" target="_blank" rel="noopener noreferrer">
          Learn React
        </a>

      </header>
    </div>
  );
}

export default App;
