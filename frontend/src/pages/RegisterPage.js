import React, { useEffect, useState } from 'react'
import { useDispatch } from 'react-redux'
import { useNavigate, Link } from 'react-router-dom'
import { ReactComponent as AuthImage2 } from '../svg/login-image2.svg'
import Form from '../components/Form'
import Input from '../components/Input'
import { registerSuccess, registerFail, cleanSubmit, submitRequest } from '../state/auth/authActions'
import { axiosInstanceUnauth } from '../axios'
import Submit from '../components/Submit'
import { useAlert } from 'react-alert'
import axios from 'axios'

const RegisterPage = () => {
  const [userInfo, setUserInfo] = useState({
    username: '',
    email: '',
    password: '',
    re_password: '',
  })
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const [validators, setValidators] = useState([]);
  const alert = useAlert();

  function handleChange(e) {
    setUserInfo({
      ...userInfo,
      [e.target.name]: e.target.value
    })
  }

  const handleSubmit = async (e) => {  
    e.preventDefault();
    dispatch(submitRequest())
    axiosInstanceUnauth.post('/auth/users/', userInfo)
      .then((response) => {
        dispatch(registerSuccess());
        navigate('/login/');
        alert.success('Registered successfully')
      })
      .catch((error) => {
        dispatch(registerFail(error.response.data));
        setValidators(error.response.data);
      })
  }

  useEffect(() => {
    return () => {
      dispatch(cleanSubmit());
    }
  })

  return (
    <React.Fragment>
      <main className='auth flex'>
        <h1 className='brand-big'>ScheduleIt!</h1>
        <Form 
          onSubmit={handleSubmit}
          validators={validators}
          onChange={handleChange}
        >
          <Input name="username" placeholder="Username"/>
          <Input name="email" placeholder="Email" type="email"/>
          <Input name="password" placeholder="Password" type="password"/>
          <Input name="re_password" placeholder="Repeat Password" type="password"/>
          <Submit className='button' value="Sign In"/>
        </Form>
        <div className="auth__links flex">
          <Link to="/login/" className="link">Already have an account? Login here!</Link>
        </div>
      </main>
      <div className="auth-image flex">
        <AuthImage2/>
      </div>
    </React.Fragment>
  )
}

export default RegisterPage