import React from 'react';
import axios from 'axios';

export default class Users extends React.Component {
    state = {
        persons: []
    }
    componentDidMount() {
        axios.get("/api/user")
            .then(res => {
                const users = res.data;
                // console.log(users);
            })

    }
    render() {
        return (
            <ul>
                <h1>Hello</h1>
            </ul>
        )
    }
}