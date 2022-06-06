import React from "react";
import {Link} from "react-router-dom";
import './App.css';

function NavBar() {
    return (<nav className="task-wrapper" id="task-container">
            <Link to="/login">Login</Link> | <Link to="/">Todos</Link> | <Link to="/accounts">Accounts</Link></nav>
)
}

export default NavBar