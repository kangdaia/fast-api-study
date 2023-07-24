/**
 * fast api backend 호출
 * @param {string} operation - get, post, put, delete 등의 api type 지정
 * @param {string} url - 요청 URL. 앞의 호스트명은 생략
 * @param {json} params - 요청 데이터 ex) {page:1, query: ...}
 * @param success_callback - 성공할때 콜백 function
 * @param failure_callback - 실패할때 콜백 function
 */
const fastapi = (operation, url, params, success_callback, failure_callback) => {
    let method = operation
    let content_type = "application/json"
    let body = JSON.stringify(params)

    let _url = import.meta.env.VITE_SERVER_URL + url
    if (method === "get") {
        _url += "?" + new URLSearchParams(params)
    }

    let options = {
        method: method,
        headers: {
            "Content-Type" : content_type
        }
    }

    fetch(_url, options)
    .then(response => {
        response.json()
        .then(json => {
            if (response.status >= 200 && response.status < 300) {
                if(success_callback) {
                    success_callback(json)
                }
            } else {
                if (failure_callback) {
                    failure_callback(json)
                }else {
                    alert(JSON.stringify(json))
                }
            }
        })
        .catch(error => {
            console.log(JSON.stringify(error))
        })
    })
}

export default fastapi