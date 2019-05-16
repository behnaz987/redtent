// module import
import React, { Component } from 'react';
import { FiUser, FiSearch, FiBox } from 'react-icons/fi';
import { NavLink } from 'react-router-dom';

// src import 


// assets import


// logic
class Header extends Component {
  render() {
    return(
      <header className="header">
        <nav >
          <NavLink exact to="/login"><FiUser /></NavLink>
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

export default Header;
