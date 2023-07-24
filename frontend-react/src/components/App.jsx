import '../assets/css/App.css'
import { Outlet } from "react-router-dom";
import { useSelector, useDispatch } from 'react-redux';


function App() {

  return (
    <>
      <header className='w-full min-w-[420px] p-5 bg-zinc-700 my-2 place-content-between'>
        <a href='/' className='px-5 py-2'>Home</a>
        <a href='/signup' className='px-5 py-2'>회원가입</a>
        { 
          <a href='/login' className='px-5 py-2'>로그인</a> 
        }
      </header>
      <Outlet/>
    </>
  )
}

export default App;
