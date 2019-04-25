// module import
import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';

// src dir import
import App from './App'

// assets import


// logic goes here
ReactDOM.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>, 
  document.querySelector('#root')
);
