import { json, redirect } from "react-router-dom";
import qs from 'qs';

async function fastAPIconn(url, operation, params) {
    let _url = import.meta.env.VITE_SERVER_URL + url
    let method = operation
    let content_type = "application/json"
    let body = JSON.stringify(params)

    if(operation === 'login') {
        method = 'post'
        content_type = 'application/x-www-form-urlencoded'
        body = qs.stringify(params)
    }

    if (method === "get") {
        _url += "?" + new URLSearchParams(params)
    }

    let options = {
        method: method,
        headers: {
            "Content-Type" : content_type
        },
    }

    const user = localStorage.getItem("user");
    if (user) {
        let data = JSON.parse(user);
        options.headers["Authorization"] = "Bearer " + data["access_token"]
    }

    if (method !== 'get') {
        options['body'] = body
    }

    return await fetch(_url, options)
        .then(response => {
            if(response.status === 204) {  // No content
                return "success"
            }
            return response.json()
        })
}

export default fastAPIconn