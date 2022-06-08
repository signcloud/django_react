import React from "react";
import {Link} from "react-router-dom";
import './App.css';
import axiosInstance from "./axios";
import {render} from "react-dom";


class Logout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            user_info: ""
        }

        this.token = localStorage.getItem("access_token")

        fetch("http://0.0.0.0/api/accounts/logout/", {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'Authorization': `JWT ${this.token}`,

            },
        }).then((response) => {
            console.log(response)
        })
    }

    // console.log(this.state.user_info)


    render() {

        return (
            <nav className="task-wrapper" id="task-container">
                Logout success!
            </nav>
        )
    }
}

export default Logout