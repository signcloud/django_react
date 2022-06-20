import React from "react";
import {Link} from "react-router-dom";
import './App.css';
import axiosInstance from "./axios";

class NavBar extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            user_info: ""
        }

        // this.user_id = this.getCookie('user')

        this.promise = axiosInstance.get(`http://${window.location.host}/api/v1/user/user/current/`);
        this.promise.then(res => this.setState({
            user_info: res.data
        }))
    }

    // console.log(this.state.user_info)


    render() {
        let user_info = this.state.user_info
        console.log(user_info)
        let login
        if (user_info.email) {
            login = `${user_info.first_name} ${user_info.last_name} (${user_info.email})`
        }
        return (
            <nav className="task-wrapper" id="task-container">
                {login} <Link to="/login">Login</Link> | <Link
                to="/">Todos</Link> | <Link to="/accounts">Accounts</Link>
            </nav>
        )
    }
}

export default NavBar