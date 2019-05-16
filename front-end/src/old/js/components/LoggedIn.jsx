import React, { Component } from 'react';
import { connect } from 'react-redux';
import { Redirect } from 'react-router-dom';

function mapStateToProps(state, ownProps) {
  return {
    isLoggedIn: (state.login.token === "") ? false : true,
  }
}

class LoggedIn extends Component {
  // constructor(mapStateToProps){
  //   super(mapStateToProps);
  // }
  // componentDidMount() {
  //   if(!isLoggedIn) {
  //     return <Redirect to='/login' />
  //   }
  // }
  render() {
    return (!mapStateToProps().isLoggedIn ? this.props.children : <Redirect to='/login' />);
  }
}

export default connect(mapStateToProps)(LoggedIn);
