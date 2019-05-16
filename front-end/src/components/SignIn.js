// module import
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { NavLink, Redirect } from 'react-router-dom';

// src dir import
import * as action from '../actions/index';

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
    const userData = {
      user_name: this.state.username,
      password: this.state.password
    };
    this.props.dispatch(action.postUserData(userData));
  }

  render() {
    if(!this.props.isLoggedIn){
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
            <div className="redirect-signin">
              <p><NavLink to="/signup">ثبت نام</NavLink></p>
            </div>
          </form>
        </div>
      );
    } else {
      return <Redirect to='/account' />
    }
  }
}

const mapStateToProps = state => {
  return {
    isLoggedIn: state.login.isLoggedIn,
    loginToken: state.login.token,
  };
} 
export default connect(mapStateToProps)(SignIn);
