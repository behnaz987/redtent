// module import
import React, { Component } from "react";
import store from '../store/index';
import { login } from '../actions/index';

// src dir import
import API from './API';

// assets import


// logic
class SignIn extends Component {
  constructor() {
    super();
    this.state = {
      username: "",
      password: ""
    }
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleUsername = this.handleUsername.bind(this);
    this.handlePassword = this.handlePassword.bind(this);
  }

  handleUsername(e) {
    this.setState(
      {username: e.target.value}
    )
  }

  handlePassword(e) {
    this.setState(
      {password: e.target.value}
    )
  }

  handleSubmit(e) {
    e.preventDefault();
    // const body = {
    //   user_name: this.state.username,
    //   password: this.state.password
    // };
    // fetch(API.Login, {
    //             method: 'POST',
    //             headers: new Headers(),
    //             body: JSON.stringify(body)
    //         }).then((res) => res.json())
    //         .then((data) =>  console.log(data))
    //         .catch((err)=>console.log(err));
    store.subscribe(() => console.log("yay!"));
    store.dispatch( login({token: "ali"}) );
  }

  render() {
    return (
      <div className="sign-in">
        <form onSubmit={this.handleSubmit}>
          <div className="username">
            <label>نام کاربری: 
              <input type="text" value={this.state.username}
                                onChange={this.handleUsername} required></input>
            </label>
          </div>
          <div className="password">
            <label>رمز عبور: 
              <input type="password" value={this.state.password}
                                onChange={this.handlePassword} required></input>
            </label>
          </div>
          <div className="submit-button">
            <button type="submit">ورود</button>
          </div>
        </form>
      </div>
    );
  }
}

export default SignIn;
