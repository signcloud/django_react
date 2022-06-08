import React from 'react';
import './App.css';
import Todo from "./Todo";
import Login from "./Login";
import Logout from "./logout";
import Accounts from "./Accounts";
import NavBar from "./NavBar";
import {Route, Routes} from 'react-router-dom'

function App() {
    return (
        <div className="App">
            <NavBar/>
            <Routes>
                <Route exact path="/login" element={<Login/>}/>
                <Route exact path="/logout" element={<Logout/>}/>
                <Route exact path="" element={<Todo/>}/>
                <Route exact path="/accounts" element={<Accounts/>}/>
            </Routes>
        </div>
    )
}

export default App