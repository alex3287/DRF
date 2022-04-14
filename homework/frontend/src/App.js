import React from 'react'
import logo from './logo.svg';
import './App.css';
import UserList from "./components/User";
import axios from "axios";


class App extends React.Component {
  constructor(props) {
      super(props);
      this.state = {
          'users': []
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
  }
  // componentDidMount() {
  //  axios
  //       .get('http://127.0.0.1:8000/api/user')
  //       .then(response => {
  //         const users = response.data
  //         this.setState(
  //             {
  //               'users': users
  //             }
  //         )
  //       })
  //       .catch(error => console.log(error))
  // }
  // componentDidMount() {
  //     const users = [
  //         {
  //             "url": "http://127.0.0.1:8000/api/users/3/",
  //             "username": "alex2",
  //             "first_name": "Alex2",
  //             "last_name": "L2",
  //             "email": "alex2@mail.ru"
  //         },
  //         {
  //             "url": "http://127.0.0.1:8000/api/users/2/",
  //             "username": "alex",
  //             "first_name": "Alex1",
  //             "last_name": "Li",
  //             "email": "alex1@mail.ru"
  //         },
  //         {
  //             "url": "http://127.0.0.1:8000/api/users/1/",
  //             "username": "al",
  //             "first_name": "Alexej",
  //             "last_name": "London",
  //             "email": "lond@mail.ru"
  //         }
  //     ]
  //     this.setState(
  //         {
  //             'users': users
  //         }
  //     )
  // }
    render() {
    return (
        <div>
          <UserList users={this.state.users} />
        </div>
    )
  }
}

export default App;
