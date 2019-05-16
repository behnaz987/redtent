// module import
import React, { Component } from 'react';
import { Route } from 'react-router-dom';

// src import
import Header from './Header';
import Footer from './Footer';
import Login from './Login';
import LoggedIn from './LoggedIn.jsx';
import Feed from './Feed.jsx';

// assets import
import '../../assets/stylesheets/app.css';


// logic
class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loggedIn: false
    }
  }

  render() {
    return(
      <div className="redtent-root">
        <Header />
        <Route path="/login" 
               component={ Login }/>
        <Route component={ LoggedIn }>
          <Route path="/feed"
                 component={ Feed } />
        </Route>
        <Footer />
      </div>
    );
  }
}

export default App;
