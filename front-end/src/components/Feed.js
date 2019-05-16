import React from 'react';
import { connect } from 'react-redux';
// import { Redirect } from 'react-router-dom';

import * as action from '../actions/index';
import Image from './Image';
import API from './API';

class Feed extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      from: 0,
      row: 10,
      bannerHeight: 0,
      freeHeight: 0,
      images: []
    }
    this.fetchImages = this.fetchImages.bind(this);
    this.banner = this.banner.bind(this);
  }

  componentWillMount() {
    this.fetchImages(0, 5);
  }

  fetchImages(from, number) {
    // get most viewd
    fetch(
      `${API.items}_from=${from}&_row=${number}&_order_by=view`, {
        method: 'GET',
        headers: new Headers(),
      }
    ).then(response => response.json())
    .then(data => {
      this.setState({images: this.getUnique(data)});
    })
    .catch(error => console.log(error));

    // get most rated
    fetch(
      `${API.items}_from=${from}&_row=${number}&_order_by=total_rate`, {
        method: 'GET',
        headers: new Headers(),
      }
    ).then(response => response.json())
    .then(data => {
      this.setState({images: this.getUnique(data)});
    })
    .catch(error => console.log(error));
  }

  getUnique(newArr) {

    const arr = [...this.state.images, ...newArr];
    const unique = arr
         .map(e => e['id'])
  
       // store the keys of the unique objects
      .map((e, i, final) => final.indexOf(e) === i && i)
  
      // eliminate the dead keys & store unique objects
      .filter(e => arr[e]).map(e => arr[e]);
    
    return unique;
  }

  eachImage(image, i) {
    return(
      <Image src={API.files + image.path}
             alt={image.title} 
             key={image.id} 
             index={i}
             id={image.id} 
             render='feed' />
    );
  }

  banner() {
    return (
      <div fill="red" 
           className="banner" >
      </div>
    );
  }

  render() {
    return(
      <div className="feed-wrapper">
        <div className="feed" style={{height: "100%"}}>
          { this.state.images.map(this.eachImage) } 
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    isLoggedIn: state.login.isLoggedIn,
    loginToken: state.login.token,
    height: state
  };
} 
export default connect(mapStateToProps)(Feed);
