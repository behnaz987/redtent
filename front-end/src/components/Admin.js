import React, { Component } from "react";
import API from "./API";

class Admin extends Component {
  constructor(props) {
    super(props);
    // action: upload, edit, delete
    this.state = {
      action: "upload",
      uploadImage: `${API.files}images.png`,
      tags: "",
      file: null
    };
    this.handleTags = this.handleTags.bind(this);
    this.uploadClick = this.uploadClick.bind(this);
    this.uploadInput = this.uploadInput.bind(this);
  }

  handleTags(e) {
    this.setState({tags: e.target.value});
  }

  uploadClick(e) {
    this.inputFileElement.click();
  }

  uploadInput(e) {
    this.setState({file: e.target.files[0]});
    const reader = new FileReader();
    reader.onload = event => {
      this.setState({uploadImage: event.target.result});
    }
    reader.readAsDataURL(e.target.files[0]);
  }

  render() {
    return(
      <div className="Admin">
        <div className="upload">
          <img src={this.state.uploadImage} 
               style={ {cursor:"pointer"} } 
               alt="images"
               onClick={ this.uploadClick }/>
          <input type="file" 
                 ref={input => this.inputFileElement = input}
                 onChange={ this.uploadInput }
                 style={ {display: "none"} } />
          <input type="text" />
          <button type="submit">ارسال</button>
        </div>
        <div className="edit"></div>
        <div className="delete"></div>
        <div className="users"></div>
        <div className="comments"></div>
        <div className="images"></div>
      </div>
    );
  }
}

export default Admin;
