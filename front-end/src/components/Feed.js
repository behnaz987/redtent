import React from 'react';
import { connect } from 'react-redux';
import { Redirect } from 'react-router-dom';

import * as action from '../actions/index';
// import Banner from './Banner';
import Image from './Image';
import API from './API';

class Feed extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      from: 0,
      row: 10,
      images: []
    }
  }

  componentWillMount() {
    fetch(
      `${API.items}`, {
        method: 'GET',
        headers: new Headers(),
      }
    ).then(response => response.json())
    .then(data => this.setState({images: data}))
    .catch(error => console.log(error));
  }

  eachImage(image, i) {
    return(
      <Image src={API.files + image.path}
             alt={image.title} 
             key={image.id} 
             index={i} 
             feed={true}
             serach={false}
             imagePage={false} />
    );
  }

  render() {
    return(
      <div className="feed-wrapper">
        {/* <Banner /> */}
        <div className="feed">
          { this.state.images.map(this.eachImage) } 
          { console.log(this.state) }
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    isLoggedIn: state.login.isLoggedIn,
    loginToken: state.login.token,
    images: state.images
  };
} 
export default connect(mapStateToProps)(Feed);
