import React, { Component } from "react";
import axios from 'axios';
import API from "./API";

class Admin extends Component {
  constructor(props) {
    super(props);
    // action: upload, edit, delete
    this.state = {
      action: "upload",
      uploadImage: `${API.files}images.png`,
      tags: "",
      file: null,
      fileResponse: null
    };
    this.handleTags = this.handleTags.bind(this);
    this.uploadInput = this.uploadInput.bind(this);
    this.submitUpload = this.submitUpload.bind(this);
    this.renderUpload = this.renderUpload.bind(this);
  }

  handleTags(e) {
    this.setState({tags: e.target.value});
  }

  uploadInput(e) {
    this.setState({file: e.target.files[0]});
    const reader = new FileReader();
    reader.onload = event => {
      this.setState({uploadImage: event.target.result});
    }
    reader.readAsDataURL(e.target.files[0]);
  }

  async submitUpload(e) {
    console.log("ya")
    e.preventDefault();
    // uploading image
    const fd = new FormData();
    fd.append('file', this.state.file);
    // getting server respnse
    const fileResponse = await fetch(API.files, {
      method: 'POST',
      headers: {'Content-Type': 'multipart/form-data', 'Accept': '*/*'},
      body: fd
    }).then(res => res.json());
    // FIX FILE UPLOAD
    // setting image
    const pic = fileResponse.path;
    const dbBody = {pic: pic}
    const dbResponse = await fetch(API.items, {
      method: 'POST',
      headers: new Headers(),
      body: JSON.stringify(dbBody)
    }).then(res => res.json());
    // setting tags
    const id = dbResponse.id;
    const tagsBody = {
      body: this.state.tags.split(/\s/)
    };
    const tagsResponse = await fetch(`${API.items}${id}/tags`, {
      method: 'POST',
      headers: new Headers(),
      body: JSON.stringify(tagsBody)
    }).then(res => res.json());
  }

  renderUpload() {
    return(
      <form className="upload"
              onSubmit={this.submitUpload}
              style={{
               direction: "ltr",
               display: "flex",
               flexDirection: "row",
               alignItems: "center",
               border: "2px solid black"
              }}>
          <div className="img-wrapper">
            <img src={this.state.uploadImage} 
                style={ {
                  cursor:"pointer",
                  width: "300px",
                  borderRadius: "8px",
                  margin: "8px",
                  border: "2px black solid"
                  } } 
                alt="images"
                onClick={ () => this.inputFileElement.click() }/>
            <input type="file" 
                  ref={input => this.inputFileElement = input}
                  onChange={ this.uploadInput }
                  style={ {display: "none"} } />
          </div>
          <div className="tags-wrapper"
               style={{
                 display: "flex",
                 flexDirection: "column",
                 alignItems: "center"
               }}>
            <textarea name="text"
                      onChange={this.handleTags}
                      style={{
                        width: "250px",
                        height: "225px",
                        backgroundColor: "beige",
                        border: "2px solid black",
                        borderRadius: "8px",
                        color: "black",
                        fontSize: "1.5rem",
                        direction: "rtl",
                        padding: "8px",
                        margin: "8px"
                      }} />
            <button type="submit"
                    style={{
                      width: "100px",
                      height: "100%",
                      padding: "8px",
                      margin: "0 8px",
                      borderRadius: "8px",
                      border: "2px solid black",
                      fontSize: "1.2rem",
                      cursor: "pointer"
                    }}>آپلود</button>
          </div>
        </form>
    );
  }
  
  render() {
    return(
      <div className="Admin">
        { this.renderUpload() }
        {/* <div className="edit"></div> */}
        {/* <div className="delete"></div> */}
        {/* <div className="users"></div>
        <div className="comments"></div>
        <div className="images"></div> */}
      </div>
    );
  }
}

export default Admin;
