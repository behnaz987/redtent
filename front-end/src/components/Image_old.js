import React, { Component } from 'react';
import { 
  FiShare2, 
  FiDownload, 
  FiHeart,
  FiPlus,
  FiFacebook, 
  FiLinkedin, 
  FiTwitter, 
  FiSend, 
  FiMail 
} from 'react-icons/fi';
import { 
  FaWhatsapp 
} from 'react-icons/fa';
// import { 
//   FacebookShareButton, 
//   LinkedinShareButton, 
//   TwitterShareButton, 
//   TelegramShareButton, 
//   WhatsappShareButton, 
//   EmailShareButton 
// } from 'react-share';
// import sizeOf from 'image-size';
import { connect } from 'react-redux';
import { NavLink } from 'react-router-dom';

class Image extends Component {
  constructor(props) {
    super(props);
    this.state = {  
      height: 0
    }

    this.renderFeed = this.renderFeed.bind(this);
    this.calculateDimention = this.calculateDimention.bind(this);
  }

  componentWillMount() {
    this.calculateDimention();
  }

  calculateDimention() {
    let freeHeight = 0;
    const windowHeight = this.props.height.window
    let occupiedHeight = 65;
    for (let k in this.props.height) {
      occupiedHeight += k === "window" ? 0 : this.props.height[k]; 
    }
    freeHeight = windowHeight - occupiedHeight;
    this.setState({height: freeHeight});
  }

  renderFeed() {
    return (
      <div className="image-wrapper"
           id={`image-${this.props.index}`}>
        <NavLink to={`/images/${this.props.key}`}>
          <img src={this.props.src}
               alt={this.props.alt} 
               style={{
                 height: this.state.height
               }}/>
        </NavLink>
      </div>
    );
  }
  
  render() {
    if(this.props.feed){
      return this.renderFeed();
    } else {
      return null;
    }
  }
}

const mapStateToProps = state => {
  return {
    isLoggedIn: state.login.isLoggedIn,
    loginToken: state.login.token,
    height: state.height
  };
} 
export default connect(mapStateToProps)(Image);
