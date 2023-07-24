import { useEffect, useState } from "react";
import fastAPIconn from '../auth/authenticate';
import { Form } from "react-router-dom";

function Profile() {
    const [ open, setOpen ] = useState(false);
    const [ profile, setProfile ] = useState({username: "", email: ""});
    const getCurrentUser = () => {
        return JSON.parse(localStorage.getItem("user"));
    };
    const loadProfile = () => {
        fastAPIconn('/api/user/profile', "get", {})
        .then((data) => {
            if (data.detail) {
                alert(data.detail);
            } else {
                console.log(data);
                setProfile(data);
            }
        })
    }
    useEffect(() => {
    const user = getCurrentUser();
    if (user) {
        setOpen(true);
        loadProfile();
    }
    }, []);
    if (!open) {
        return (
            <div className="text-white py-5 px-8 flex flex-col bg-zinc-700 min-w-[420px]">
                회원 전용 페이지입니다. <a href="/login">로그인하기</a>
            </div>
        );
    }
    return (
        <div className="text-white py-5 px-8 flex flex-col bg-zinc-700 min-w-[420px]">
            <Form className="grid grid-col justify-items-stretch gap-5 my-2">
                <label className="grid grid-row gap-2 text-left">
                    <b>Username</b>
                    <input className="bg-zinc-800 p-2"
                        name="username"
                        type="text"
                        value={profile.username}
                        placeholder={profile.username}
                    />
                </label>
                <label className="grid grid-row gap-2 text-left">
                    <b>Email</b>
                    <input className="bg-zinc-800 p-2"
                        name="email"
                        type="email"
                        value={profile.email}
                        placeholder={profile.email}
                    />
                </label>
            </Form>
        </div>
    );
}

export default Profile;