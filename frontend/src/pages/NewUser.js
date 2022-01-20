import axios from 'axios'
import React, { useState, useEffect } from 'react'

export default function NewUser() {
    // Getter and setter for user state
    // const [user, setUser] = useState([]);
    const [name, setName] = useState("");

    //Using  useEffect to reatrive data from an API (similar to componentDidMount in a class)
    // const data = {
    //     "name": name,
    //     "extra_info": {
    //         "items": {
    //             "qty": 8,
    //             "product": "Phone"
    //         },
    //         "customer": "Cruz"
    //     }
    // }

    const data = {
        "name": name,
        "extra_info": {
        }
    }
    useEffect(() => {


        // postUser()
    }, []) // Don't forget the `[]`, which will prevent use Effect from running in an infinite loop
    const postUser = async () => {
        console.log("data")
        console.log(data)
        const response = await axios.post('http://127.0.0.1:8000/api/role', data)
    }
    // console.log(name)
    const handleSubmit = (event) => {
        event.preventDefault();
        postUser()
    }

    // Return a tabel
    return (
        <div className="container" >
            <h1>New User</h1>
            <form onSubmit={handleSubmit}>
                <label>Name Role:
                    <input type="text"
                        value={name}
                        onChange={(e) => setName(e.target.value)} />
                </label>
                <input type="submit" value="Submit" />
            </form>
        </div >

    );
}