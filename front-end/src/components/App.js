import React, { Component } from "react";
import { Route } from 'react-router-dom';

import Header from './Header';
import SignUp from './SignUp';
import SignIn from './SignIn';
import Footer from './Footer';
import Feed from './Feed';
import Image from './Image';

class App extends Component {
  render() {
    return (
    <div className="redtent-root">
      <Header />
        <Route path="/signup" component={ SignUp } />
        <Route path="/signin" component={ SignIn } />
        <Route exact path="/feed" component={ Feed } />
        <Route path="/images" component={ Image } />
      <Footer />
    </div>
    );
  }
}

export default App;
