import { json, redirect } from "react-router-dom";

async function fastAPIconn(url, operation, params) {
    let _url = import.meta.env.VITE_SERVER_URL + url
    let body = JSON.stringify(params)

    if (operation === "get") {
        _url += "?" + new URLSearchParams(params)
    }

    let options = {
        method: operation,
        headers: {
            "Content-Type" : "application/json"
        },
    }

    if (operation !== 'get') {
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