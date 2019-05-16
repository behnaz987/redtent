// module import
import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import { Provider } from "react-redux";

// src dir import
import App from './components/App';
import store from "./store/index";

// assets import
import './assets/stylesheets/index.css';

// logic goes here
ReactDOM.render(
  <Provider store={ store }>
    <BrowserRouter>
      <App />
    </BrowserRouter>
  </Provider>, 
  document.querySelector('#root')
);

