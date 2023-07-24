import { useState } from 'react'
import '../../index.css'
import { Form } from "react-router-dom";
import fastAPIconn from '../../auth/authenticate';

function SignUpComp() {
    const [password, setPassword] = useState("");
    const [passwordcheck, setPasswordcheck] = useState();

    const handleChangePS = (e) => {
        setPassword(e.target.value)
        setPasswordcheck(false)
    }

    const handleChangePSValidate = (e) => {
        if (e.target.value === "") {
            setPasswordcheck(undefined)
        } else {
            setPasswordcheck(e.target.value === password)
        }
    }

    function handleSubmit(e) {
        // Prevent the browser from reloading the page
        e.preventDefault();
    
        const form = e.target;
        const formData = new FormData(form);
        let params = {
            username: formData.get("username"),
            email: formData.get("email"),
            password1: formData.get("password1"),
            password2: formData.get("password2")
        }

        fastAPIconn('/api/user/signup', form.method, params)
        .then((data) => {
            if (data === "success") {
                alert("회원가입이 완료되었습니다.")
            } else {
                console.log(data["detail"][0].msg)
                alert(data["detail"][0].msg)
            }
        })
    }

    const CheckList = ({value}) => {
        const passwordRules = [
            {label:"문자 8자 이상", pattern: new RegExp(/.{8,}$/)},
            {label:"대문자 1개 이상 및 숫자 1개 이상 포함", pattern: new RegExp(/(?=.*[\d])(?=.*[A-Z])/)},
            {label:"특수문자[!@#$%^&+=?.] 1개 이상 포함", pattern: new RegExp(/.*[!@#$%^&+=?.]/)},
        ]
        if (password) {
            return (
                <ul>
                    {
                        passwordRules.map((rule, i) => {
                            const cn = value && value.match(rule.pattern)? "pass text-green-500": "fail text-red-500";
                            return <li key={i} className={cn}>{cn.includes("pass")? <i className="fa-solid fa-check"></i>:null} {rule.label}</li>
                        })
                    }
                </ul>
            );
        } else {
            return (<></>);
        }
    }

    return (
        <div className="text-white py-5 px-8 flex flex-col bg-zinc-700 min-w-[420px]">
            <h1 className="p-2 text-xl text-center font-bold">회원가입</h1>
            <Form method="post" onSubmit={handleSubmit} className="grid grid-col justify-items-stretch gap-5 my-2">
                <label className="grid grid-row gap-2 text-left">
                    <b>Username</b>
                    <input className="bg-zinc-800 p-2"
                        name="username"
                        type="text"
                        required
                    />
                </label>
                <label className="grid grid-row gap-2 text-left">
                    <b>Email</b>
                    <input className="bg-zinc-800 p-2"
                        name="email"
                        type="email"
                        required
                    />
                </label>
                <label className="grid grid-row gap-2 text-left">
                    <b>비밀번호</b>
                    <CheckList value={password}/>
                    <input className="bg-zinc-800 p-2"
                        name="password1"
                        type="password"
                        onChange={handleChangePS}
                        required
                    />
                </label>
                <label className="grid grid-row gap-2 text-left">
                    <b>비밀번호 확인</b>
                    <input className="bg-zinc-800 p-2"
                        name="password2"
                        type="password"
                        onChange={handleChangePSValidate}
                        required
                    />
                    {
                        passwordcheck != undefined ? 
                            <p className={passwordcheck? "text-green-500": "text-red-500"}>{(passwordcheck)? "비밀번호가 일치합니다.": "비밀번호가 일치하지 않습니다."}</p>
                        : null
                    }
                </label>
                <button type="submit" className="bg-zinc-600 px-5 py-2 flex-shrink my-2.5 text-white">가입하기</button>
            </Form>
            <p className='py-2.5 mt-2.5'>
                이미 계정이 있다면? <a href='/login'>로그인</a>
            </p>
        </div>
    );
}

export default SignUpComp;