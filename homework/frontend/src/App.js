import React from 'react'
// import './App.css';
import axios from "axios";
import UserList from "./components/UserList";
import ToDoList from "./components/ToDoList";
import ProjectList from "./components/ProjectList";
import {BrowserRouter, Route, Routes, Link, Navigate, useLocation} from "react-router-dom";


const NotFound = () => {
    var locateion = useLocation()
    return (
        <div>
            Page "{locateion.pathname}" not found
        </div>
    )
}

class App extends React.Component {
  constructor(props) {
      super(props);
      this.state = {
          'users': [],
          'projects': [],
          'notes': [],
      }
  }
  componentDidMount() {
      axios
        .get('http://127.0.0.1:8000/api/users/')
        .then(response => {
          const users = response.data
          this.setState(
              {
                'users': users
              }
          )
        })
        .catch(error => console.log(error))
      axios
        .get('http://127.0.0.1:8000/api/projects/')
        .then(response => {
          const projects = response.data
          this.setState(
              {
                'projects': projects
              }
          )
        })
        .catch(error => console.log(error))
      axios
        .get('http://127.0.0.1:8000/api/note/')
        .then(response => {
          const notes = response.data
          this.setState(
              {
                'notes': notes
              }
          )
        })
        .catch(error => console.log(error))
  }

    render() {
    return (
        <div>
           <BrowserRouter>
               <nav>
                    <ul>
                        <li><Link to='/'>Главная</Link></li>
                        <li><Link to='/users'>Список Пользователи</Link></li>
                        <li><Link to='/projects'>Список Проекты</Link></li>
                        <li><Link to='/note'>Список ToDo</Link></li>
                    </ul>
                </nav>
               <Routes>
                   <Route exact path='/' element={<UserList users={this.state.users} />}/>
                   {/*<Route exact path='/users' element={<UserList users={this.state.users}/>}/>*/}
                   <Route exact path='/users' element={<Navigate to='/' />}/>
                   <Route exact path='/projects' element={<ProjectList projects={this.state.projects} />}/>
                   <Route exact path='/note' element={<ToDoList notes={this.state.notes} />}/>
                   <Route exact path='*' element={<NotFound/>}/>
               </Routes>
           </BrowserRouter>

        </div>
    )
  }
}

export default App;
