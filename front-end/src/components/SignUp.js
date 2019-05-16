// module import
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { NavLink, Redirect } from 'react-router-dom';

// src dir import
import * as action from '../actions/index';

// assets import


// logic
class SignUp extends Component {
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
    const type = "SIGNUP";
    this.props.dispatch(action.postUserData(userData, type));
    this.setState({loggedIn: true});
  }

  render() {
    if (!this.props.isloggedIn){
      return (
        <div className="sign-up">
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
              <button type="submit">ثبت نام</button>
            </div>
            <div className="redirect-signin">
              <p>قبلا <NavLink to="/signin">ثبت نام</NavLink> کرده اید.</p>
            </div>
          </form>
        </div>
      );
    } else {
        return <Redirect to='/account' />;
    }
  }
}

const mapStateToProps = state => {
  return {
    isLoggedIn: state.login.isLoggedIn,
    loginToken: state.login.token
  };
} 
export default connect(mapStateToProps)(SignUp);
