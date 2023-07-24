import { useState } from 'react'
import '../App.css'

function LoginComp() {
    return (
        <div className="text-white rounded-lg py-5 px-8 flex flex-col bg-zinc-700 min-w-[420px]">
            <h1 className="p-2 text-xl text-center font-bold">Login Page</h1>
            <form method="POST" className="grid grid-col justify-items-stretch gap-2.5 my-2">
                <label className="grid grid-row gap-2 text-left">
                    <b>Username</b>
                    <input className="bg-zinc-800 p-2 rounded-lg"
                        name="username"
                    />
                </label>
                <label className="grid grid-row gap-2 text-left">
                    <b>비밀번호</b>
                    <input className="bg-zinc-800 p-2 rounded-lg"
                        name="password"
                        type="password"
                    />
                </label>
                <button type="submit" className="bg-zinc-600 rounded-lg px-5 py-2 flex-shrink my-2.5">로그인</button>
            </form>
        </div>
    );
}

export default LoginComp;