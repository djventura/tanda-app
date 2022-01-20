import React, { useState, useEffect } from 'react'
import axios from 'axios'

export default function UserPage(props) {
    //Setting initial state
    // const initialUserState = {
    //     user: {},
    //     loading: true
    // }
    // Getter and setter for user state
    // const [user, setUser] = useState(initialUserState)
    const [user, setUser] = useState([]);

    //Using  useEffect to reatrive data from an API (similar to componentDidMount in a class)
    useEffect(() => {
        const getUser = async () => {
            //Pass our param  to the API call
            const { data } = await axios(
                'http://127.0.0.1:8000/api/user'
            )

            //Update state
            setUser(data)
            // console.log(data[1].last_name)
        }
        // Invoke the async function
        getUser()
    }, []) // Don't forget the `[]`, which will prevent use Effect from running in an infinite loop


    // Return a tabel  with some data from the API.
    return (
        <div className="container" >
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Last Name</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        {user.map(data => (
                            <td key={data._id}>{data.first_name}</td>
                        ))}
                    </tr>
                </tbody>

            </table>
        </div >

    );
}