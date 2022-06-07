import SignIn from './components/login'
import NavBar from "./NavBar";
import {Route, Routes} from "react-router-dom";
import Todo from "./Todo";
import Accounts from "./Accounts";
import React from "react";

function Login() {
    return (
        <SignIn/>
    )
}

export default Login
// import React from 'react';
// import './App.css';
//
//
// class Accounts extends React.Component {
//     constructor(props) {
//         super(props);
//         this.state = {
//             accountsList: [],
//             activeItem: {
//                 id: null,
//                 first_name: '',
//                 last_name: '',
//                 mobile: '',
//                 email: '',
//                 password: '',
//             },
//             editing: false,
//         }
//         this.handleChange = this.handleChange.bind(this)
//         this.handleSubmit = this.handleSubmit.bind(this)
//         this.getCookie = this.getCookie.bind(this)
//     };
//
//     getCookie(name) {
//         let cookieValue = null;
//         if (document.cookie && document.cookie !== '') {
//             let cookies = document.cookie.split(';');
//             for (let i = 0; i < cookies.length; i++) {
//                 let cookie = cookies[i].trim();
//                 // Does this cookie string begin with the name we want?
//                 if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                     cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                     break;
//                 }
//             }
//         }
//         return cookieValue;
//     }
//
//     componentWillMount() {
//         this.fetchUsers()
//     }
//
//     fetchUsers() {
//         console.log('Fetching...')
//
//         fetch('http://0.0.0.0/api/accounts/user_list/')
//             .then(response => response.json())
//             .then(data => {
//                 this.setState({
//                     accountsList: data
//                 })
//                 console.log(data)
//             })
//     }
//
//     handleChange(e) {
//         if (e.target.name == "username") {
//             this.state.activeItem.username = e.target.value
//         } else if (e.target.name == "email") {
//             this.state.activeItem.email = e.target.value
//         } else if (e.target.name == "password") {
//             this.state.activeItem.password = e.target.value
//         } else if (e.target.name == "first_name") {
//             this.state.activeItem.first_name = e.target.value
//         } else if (e.target.name == "last_name") {
//             this.state.activeItem.last_name = e.target.value
//         } else if (e.target.name == "mobile") {
//             this.state.activeItem.mobile = e.target.value
//         }
//         this.setState({
//             activeItem: {
//                 ...this.state.activeItem
//             }
//         })
//     }
//
//     handleSubmit(e) {
//
//         console.log(JSON.stringify(this.state.activeItem))
//         e.preventDefault()
//         console.log('ITEM:', this.state.activeItem)
//
//         let csrftoken = this.getCookie('csrftoken')
//
//         let url = 'http://0.0.0.0/api/accounts/user_create/'
//
//         if (this.state.editing == true) {
//
//             url = `http://0.0.0.0/api/accounts/user_update/${this.state.activeItem.id}/`
//             console.log(url)
//             this.setState({
//                 editing: false
//             })
//         }
//
//
//         console.log(JSON.stringify(this.state.activeItem))
//
//         fetch(url, {
//             method: 'POST',
//             headers: {
//                 'Content-type': 'application/json',
//                 'X-CSRFToken': csrftoken,
//             },
//             body: JSON.stringify(this.state.activeItem)
//         }).then((response) => {
//             this.fetchUsers()
//             this.setState({
//                 activeItem: {
//                     id: null,
//                     username: '',
//                     email: '',
//                     password: '',
//                 }
//             })
//         }).catch(function (error) {
//             console.log('ERROR:', error)
//         })
//
//     }
//
//
//
//     render() {
//         let users = this.state.accountsList
//         let self = this
//         return (
//             <div className="container">
//                 <div id="task-container">
//                     <div id="form-wrapper">
//                         <form onSubmit={this.handleSubmit} id="form">
//                             <div className="flex-wrapper">
//                                 <div style={{flex: 6}}>
//                                     <input onChange={this.handleChange} className="form-control" id="email"
//                                            value={this.state.activeItem.email}
//                                            type="email" name="email"
//                                            placeholder="Email"/>
//                                     <br/>
//                                     <input onChange={this.handleChange} className="form-control" id="password"
//                                            value={this.state.activeItem.password}
//                                            type="password" name="password"
//                                            placeholder="Password"/>
//                                     <br/>
//                                     <input id="submit" className="btn btn-warning" type="submit" name="Add"/>
//                                 </div>
//                             </div>
//                         </form>
//                     </div>
//                 </div>
//             </div>
//         )
//     }
// }
//
//
// export default Accounts;
