import React from 'react'
import { Route, Switch } from 'react-router-dom'
// import './App.css';
// import axios from 'axios';
// We will create these two page in a moment
import HomePage from './pages/HomePage'
import UserPage from './pages/UserPage'
import NewUser from './pages/NewUser'

export default function App() {
  return (
    <Switch>
      <Route exact path="/" component={HomePage} />
      <Route path="/UserPage" component={UserPage} />
      <Route path="/newuser" component={NewUser} />
    </Switch>
  )
}
