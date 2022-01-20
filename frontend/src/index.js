import React from 'react';
// import ReactDOM from 'react-dom';
import { render } from 'react-dom'
import { BrowserRouter } from 'react-router-dom'
import 'bootstrap/dist/css/bootstrap.css';
import './index.css';
import App from './App';
// import Main from './Main';
// import reportWebVitals from './reportWebVitals';

render(
  <BrowserRouter>
    <App />
  </BrowserRouter>,
  document.getElementById('root')
);
