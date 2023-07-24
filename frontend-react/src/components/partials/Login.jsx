import { useState } from 'react'
import '../../index.css'
import fastAPIconn from '../../auth/authenticate';
import { Form } from 'react-router-dom';
import { useSelector } from 'react-redux';

function LoginComp() {
    function handleSubmit(e) {
        // Prevent the browser from reloading the page
        e.preventDefault();
    
        const form = e.target;
        const formData = new FormData(form);
        let params = {
            username: formData.get("username"),
            password: formData.get("password")
        }

        fastAPIconn('/api/user/login', 'login', params)
        .then((data) => {
            if (data.detail) {
                alert(data.detail)
            } else {
                console.log(data.access_token)
            }
        })
    }

    return (
        <div className="text-white py-5 px-8 flex flex-col bg-zinc-700 min-w-[420px]">
            <h1 className="p-2 text-xl text-center font-bold">Login Page</h1>
            <Form method="POST" onSubmit={handleSubmit} className="grid grid-col justify-items-stretch gap-5 my-2">
                <label className="grid grid-row gap-2 text-left">
                    <b>Username</b>
                    <input className="bg-zinc-800 p-2"
                        name="username"
                        type="text"
                        required
                    />
                </label>
                <label className="grid grid-row gap-2 text-left">
                    <b>비밀번호</b>
                    <input className="bg-zinc-800 p-2"
                        name="password"
                        type="password"
                        required
                    />
                </label>
                <button type="submit" className="bg-zinc-600 px-5 py-2 flex-shrink my-2.5">로그인</button>
            </Form>
            <p className='py-2.5 mt-2.5'>
                아직 회원이 아니라면? <a href='/signup'>회원가입</a>
            </p>
        </div>
    );
}

export default LoginComp;