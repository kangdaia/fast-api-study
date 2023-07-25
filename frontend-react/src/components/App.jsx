import '../assets/css/App.css'
import { Outlet } from "react-router-dom";
import { useState, useEffect } from 'react';


function App() {
  const [currentUser, setCurrentUser] = useState(undefined);
  const logout = () => {
    localStorage.removeItem("user");
    setCurrentUser(undefined);
    window.location.reload();
  };
  const getCurrentUser = () => {
    return JSON.parse(localStorage.getItem("user"));
  };

  useEffect(() => {
    const user = getCurrentUser();
    if (user) {
      setCurrentUser(user);
    }
    return (
      localStorage.removeItem("user")
    )
  }, []);

  return (
    <>
      <header className='w-full min-w-[420px] p-5 bg-zinc-700 my-2 place-content-between'>
        <a href='/' className='px-5 py-2'>Home</a>
        <a href='/signup' className='px-5 py-2'>회원가입</a>
        {
          currentUser?
          <button className='px-5 py-2' onClick={logout}>로그아웃</button>:
          <a href='/login' className='px-5 py-2'>로그인</a> 
        }
      </header>
      <Outlet/>
    </>
  )
}

export default App;
