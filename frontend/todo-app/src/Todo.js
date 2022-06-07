import React from 'react';
import './App.css';


class Todo extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            todoList: [], activeItem: {
                id: null, title: '', completed: false,
            }, editing: false,
        }
        this.fetchTasks = this.fetchTasks.bind(this)
        this.handleChange = this.handleChange.bind(this)
        this.handleSubmit = this.handleSubmit.bind(this)
        this.getCookie = this.getCookie.bind(this)


        this.startEdit = this.startEdit.bind(this)
        this.deleteItem = this.deleteItem.bind(this)
        this.strikeUnstrike = this.strikeUnstrike.bind(this)

        this.token = localStorage.getItem('access_token')

    };

    getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            let cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    componentWillMount() {
        this.fetchTasks()
    }

    saveToken(token) {
        localStorage.setItem('access_token', JSON.stringify(token));
    }

    refreshToken(token) {
        console.log("Refreshing")
        return fetch('/api/token/refresh', {
            method: 'POST',
            credentials: 'include',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                token,
            }),
        })
            .then((res) => {
                if (res.status === 200) {
                    const tokenData = res.json();
                    this.saveToken(JSON.stringify(tokenData));
                    console.log(tokenData)
                    return Promise.resolve();
                }
                return Promise.reject();
            });
    }

    fetchTasks() {
        const token = localStorage.getItem('access_token')

        // eslint-disable-next-line no-restricted-globals
        if (!this.getCookie("sessionid")) {
            // alert("No cookie");
            // window.location.replace("/login");
        }
        console.log('Fetching...')

        fetch('http://0.0.0.0/api/task-list/', {
            method: 'GET',
            headers: {
                'Content-type': 'application/json',
                'Authorization': `JWT ${token}`,
            },
        })
            .then(response => response.json())
            .then(data => this.setState({
                todoList: data
            }))
        console.log("Todo list: ", this.state.todoList)
        // if (this.state.todoList.length == 0) {
        //     console.log("Lenth 0")
        //     this.refreshToken(localStorage.getItem("refresh_token"))
        //     this.fetchTasks()
        // }
    }

    handleChange(e) {
        let name = e.target.name
        let value = e.target.value
        console.log('Name:', name)
        console.log('Value:', value)

        this.setState({
            activeItem: {
                ...this.state.activeItem, title: value
            }
        })
    }

    handleSubmit(e) {
        e.preventDefault()
        console.log('ITEM:', this.state.activeItem)

        let csrftoken = this.getCookie('csrftoken')

        let url = 'http://0.0.0.0/api/task-create/'

        if (this.state.editing === true) {
            url = `http://0.0.0.0/api/task-update/${this.state.activeItem.id}/`
            this.setState({
                editing: false
            })
        }


        fetch(url, {
            method: 'POST', headers: {
                'Content-type': 'application/json', 'X-CSRFToken': csrftoken,
                'Authorization': `JWT ${this.token}`,
            }, body: JSON.stringify(this.state.activeItem)
        }).then((response) => {
            this.fetchTasks()
            this.setState({
                activeItem: {
                    id: null, title: '', completed: false,
                }
            })
        }).catch(function (error) {
            console.log('ERROR:', error)
        })

    }

    startEdit(task) {
        this.setState({
            activeItem: task, editing: true,
        })
    }


    deleteItem(task) {
        let csrftoken = this.getCookie('csrftoken')

        fetch(`http://0.0.0.0/api/task-delete/${task.id}/`, {
            method: 'DELETE', headers: {
                'Content-type': 'application/json', 'X-CSRFToken': csrftoken,
                'Authorization': `JWT ${this.token}`,
            },
        }).then((response) => {

            this.fetchTasks()
        })
    }


    strikeUnstrike(task) {

        task.completed = !task.completed
        let csrftoken = this.getCookie('csrftoken')
        let url = `http://0.0.0.0/api/task-update/${task.id}/`
        // eslint-disable-next-line no-restricted-globals
        const token = this.token
        console.log("Token ", token)
        console.log("Tasd ID ", task.id)
        console.log("URL ", url)
        console.log("Completed ", task.completed)

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-type': 'application/json', 'X-CSRFToken': csrftoken,
                'Authorization': `JWT ${token}`,
            }, body: JSON.stringify({'completed': task.completed, 'title': task.title})
        }).then(() => {
            this.fetchTasks()
        })

        console.log('TASK:', task.completed)
    }


    render() {
        let tasks = this.state.todoList
        let self = this
        return (<div className="container">
            <div id="task-container">
                <div id="form-wrapper">
                    <form onSubmit={this.handleSubmit} id="form">
                        <div className="flex-wrapper">
                            <div style={{flex: 6}}>
                                <input onChange={this.handleChange} className="form-control" id="title"
                                       value={this.state.activeItem.title} type="text" name="title"
                                       placeholder="Add task.."/>
                            </div>

                            <div style={{flex: 1}}>
                                <input id="submit" className="btn btn-warning" type="submit" name="Add"/>
                            </div>
                        </div>
                    </form>

                </div>

                <div id="list-wrapper">
                    {tasks.map(function (task, index) {
                        return (<div key={index} className="task-wrapper flex-wrapper">

                            <div onClick={() => self.strikeUnstrike(task)} style={{flex: 7}}>

                                {task.completed == false ? (<span>{task.title}</span>

                                ) : (

                                    <strike>{task.title}</strike>)}

                            </div>

                            <div style={{flex: 1}}>
                                <button onClick={() => self.startEdit(task)}
                                        className="btn btn-sm btn-outline-info">Edit
                                </button>
                            </div>

                            <div style={{flex: 1}}>
                                <button onClick={() => self.deleteItem(task)}
                                        className="btn btn-sm btn-outline-dark delete">-
                                </button>
                            </div>

                        </div>)
                    })}
                </div>
            </div>

        </div>)
    }
}


export default Todo;
