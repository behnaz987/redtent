// module import
import React, { Component } from 'react';
import { connect } from 'react-redux';

// src import 
import * as action from '../actions/index'

// assets import


// logic
class Footer extends Component {
  componentDidMount() {
    this.props.dispatch(action.getFreeHeight({footer: this.divElement.clientHeight}))
  }

  render() {
    return(
      <footer className="footer"
              ref={ (divElement) => this.divElement = divElement}>
        <p>&copy; 2019</p>
      </footer>
    );
  }
}

const mapStateToProps = state => {
  return {
    isLoggedIn: state.login.isLoggedIn,
    loginToken: state.login.token,
    height: state.height
  };
} 
export default connect(mapStateToProps)(Footer);
