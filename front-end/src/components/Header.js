// module import
import React, { Component } from 'react';
import { FiUser, FiSearch, FiBox } from 'react-icons/fi';
import { connect } from 'react-redux';
import { NavLink } from 'react-router-dom';

// src import 
import * as action from '../actions/index'

// assets import


// logic
class Header extends Component {
  componentDidMount() {
    this.props.dispatch(action.getFreeHeight({window: window.innerHeight}))
    this.props.dispatch(action.getFreeHeight({header: this.divElement.clientHeight}))
    window.addEventListener(
      "resize", 
      () => this.props.dispatch(action.getFreeHeight({window: window.innerHeight}))
    );
  }
  
  render() {
    return(
      <header className="header"
              ref={ (divElement) => this.divElement = divElement}>
        <nav >
          <NavLink exact to={this.props.isLoggedIn ? '/account' : '/signin'}><FiUser /></NavLink>
          <NavLink exact to="/feed"><FiBox /></NavLink>
          <NavLink exact to="/search"><FiSearch /></NavLink>
        </nav>
        <div className="logo-container">
          <NavLink exact to="/"><FiBox className="logo" /></NavLink>
        </div>
      </header>
    );
  }
}


const mapStateToProps = state => {
  return {
    isLoggedIn: state.login.isLoggedIn,
    loginToken: state.login.token
  };
} 
export default connect(mapStateToProps)(Header);
