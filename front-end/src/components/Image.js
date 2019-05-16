import React, { Component } from 'react';
import { 
  FiDownload,
  FiPlus,
  FiFileText,
  FiMessageSquare,
  FiHeart,
  FiFacebook,
  FiTwitter,
  FiInstagram, 
  FiX,
  FiImage,
  FiList,
  FiSend, 
  FiShare2 
} from 'react-icons/fi';
import { 
  FaWhatsapp,
  FaTelegramPlane 
} from 'react-icons/fa';

import API from './API';
import Header from './Header';

class Image extends Component {

    constructor(props) {
        super(props);
        this.state = {
  
          style_comments:{},
          style_tailors:{},
          style_menu:{},
          
          style_i1:{backgroundColor: 'rgb(211, 22, 22)'},
          style_i2:{},
          style_i3:{},
          comments: [
            {
            name: 'زهرا',
            comment: "بد نیست ",
            }, {
              name: 'فائزه',
              comment: "خوبه ",
            }
          ],
          tailors:[
            { name: 'خانوم ظهیری'},
            { name: 'خانوم زمانی'}
          ],
          image: {
            url: "",
            id: "",
            rate: 0,
            view: 0
          }
        };
        this.open_tailors=this.open_tailors.bind(this);
        this.open_comments=this.open_comments.bind(this);
        this.open_img=this.open_img.bind(this);
        this.open_menu=this.open_menu.bind(this);
        this.close_menu=this.close_menu.bind(this);
      }

      open_menu() {
        this.setState({ style_menu: {height:'20%'} })
      }

      close_menu() {
        this.setState({ style_menu:{height:'0%'} })
      }
      
      open_tailors() {
        this.setState({
          style_menu: {height:'0%'},
          style_i1: {backgroundColor: 'rgb(240, 239, 239)'},
          style_i2: {backgroundColor: 'rgb(240, 239, 239)'},
          style_i3: {backgroundColor: 'rgb(211, 22, 22)'},
          style_comments: {height: '0%'},
          style_tailors: {height: '100%'}
        })
      }

      open_comments() {
        this.setState({
          style_menu: {height:'0%'},
          style_i1: {backgroundColor: 'rgb(240, 239, 239)'},
          style_i3: {backgroundColor: 'rgb(240, 239, 239)'},
          style_i2: {backgroundColor: 'rgb(211, 22, 22)'},
          style_comments:{height: '100%'},
          style_tailors:{height: '0%'}
        })
      }

      open_img(){
        this.setState({
          style_menu: {height:'0%'},
          style_i3: {backgroundColor: 'rgb(240, 239, 239)'},
          style_i2: {backgroundColor: 'rgb(240, 239, 239)'},
          style_i1: {backgroundColor: 'rgb(211, 22, 22)'},
          style_comments: {height: '0%'},
          style_tailors:{height: '0%'}
        })
      }

  // test() {
  //   const id = this.props.location.pathname.split(/\//).pop();
  //   // src
  //   // alt
  //   // comment
  //   // rate
  //   // tailor_list
  //   fetch(API.items + id, {
  //     method: 'GET',
  //     headers: new Header()
  //   }).then(response => response.json())
  //   .then(data => this.setState(data))
  //   .catch(error => console.log(error));


  // }
  componentWillMount(){
    const id = this.props.location.pathname.split(/\//).pop();
    fetch(API.items + id, {
      method: 'GET',
      headers: new Headers()
    }).then(response => response.json())
    .then(data => {
      this.setState({
        image: {
          url: API.files + data.design_picture,
          id: data.design_id,
          rate: data.total_rate,
          view: data.view,
          alt: data.design_picture
        }
      })
    })
    .catch(error => console.log(error));


  }
  render () {
    return (
      <div className="image-component">
      {console.log(this.state)}
        <div className="comment-list-image">
          <div className="icon" style={this.state.style_i1} onClick={this.open_img}>
            <FiImage />
          </div>
          <div className="icon" style={this.state.style_i2} onClick={this.open_comments}>
            <FiMessageSquare />
          </div>
          <div className="icon" onClick={this.open_tailors} style={this.state.style_i3}>
            <FiFileText />
          </div>
        </div>

        <div className="img-container">
          <img src={ this.state.image.url } 
               alt={ this.state.image.alt } 
               className="img" />
          <div className="comments" style={this.state.style_comments}>
            <div className="comment">
              <a href="#www">{this.state.comments[0].name}</a>
              <p className="comm">{this.state.comments[0].comment}</p>
            </div>

            <div className="comment">
              <p className="comm">{this.state.comments[1].comment}</p>
            </div>
            <div className="comment-input">
              <input type="text" className="in"></input>
              <FiSend className="send" />
            </div>
          </div>

          <div className="tailors" style={this.state.style_tailors}>
            <div className="tailor">
              <a href="#w">{this.state.tailors[0].name}</a>
            </div>
            <div className="tailor">
              <a href="#w">{this.state.tailors[1].name}</a>
            </div>
          </div>

          <div className="menu_share" style={this.state.style_menu}>
            <FiFacebook className="icon_" />
            <FiInstagram className="icon_" />
            <FaTelegramPlane className="icon_" />
            <FaWhatsapp className="icon_" />
            <FiTwitter className="icon_" />
            <div className="close_menu" onClick={this.close_menu}>
              <FiX />
            </div>
          </div>
        </div>


        <div className="like-menu">
          <div className="like_container">
            <FiHeart className="like" id="like1" style={this.state.like1}
              onClick={this.changeLike1} />
            <FiHeart className="like" id="like2" style={this.state.like2}
              onClick={this.changeLike2} />
            <FiHeart className="lik" id="like3" style={this.state.like3}
              onClick={this.changeLike3} />
            <FiHeart className="like" id="like4" style={this.state.like4}
              onClick={this.changeLike4} />
            <FiHeart className="like" id="like5" style={this.state.like5}
              onClick={this.changeLike5} />

          </div>
          <div className="menu_container">
            <FiDownload className="icon_" />
            <FiPlus className="icon_" />
            <FiList className="icon_" />
            <FiShare2 className="icon_" onClick={this.open_menu} />
          </div>
        </div>

      </div>
    );


}
}

export default Image;
