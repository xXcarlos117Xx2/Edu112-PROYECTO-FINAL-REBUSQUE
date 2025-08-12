import React, { useState } from 'react'
import { Link } from 'react-router-dom'

export const RegisterForm = ({ isLoginType }) => {

  const [inputs, setInputs] = useState({
    fullName: '',
    email: '',
    password: ''
  });

  function sendData() {
    if (isLoginType) {
      // Handle login logic
      const dataToSend = { email: inputs.email, password: inputs.password };
      console.log("Logging in with:", dataToSend);
    } else {
      // Handle signup logic
      console.log("Signing up with:", inputs);
    }
  }


  return (
    <div className='container'>

      <form className=' me-5'>
        {!isLoginType && (<div className="mb-4 col-8">
          <label for="exampleInputEmail1" className="form-label">Full Name</label>
          <input type="text" className="form-control" id="exampleInputFullName" placeholder='Full Name' />
        </div>)}

        <div className="mb-4 col-8">
          <label for="exampleInputPassword1" className="form-label">Email</label>
          <input type="email" className="form-control" id="exampleInputEmail1" placeholder='Email' />
        </div>

        <div className="mb-4 col-8">
          <label for="exampleInputPassword1" className="form-label">Password</label>
          <input type="password" className="form-control" id="exampleInputPassword1" placeholder='Password' />
        </div>

        <div className="d-grid gap-2 col-12 mx-auto mb-3">
          <button onClick={() => sendData()} type="button" class="btn btn-success col-8">{isLoginType ? "Login" : "Sign up"}</button>
        </div>

        {isLoginType ?
          <Link to="/auth/signup">Create a new account</Link> :
          <Link to="/auth/login">Already have an account?</Link>
        }

      </form>


    </div>


  )
}
