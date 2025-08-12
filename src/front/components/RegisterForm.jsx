import React from 'react'

export const RegisterForm = ({ isLoggedIn }) => {



  return (
    <div className='container'>

      <form className=' me-5'>
        {!isLoggedIn && (<div className="mb-4 col-8">
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
          <button type="button" class="btn btn-success col-8">{isLoggedIn ? "Login" : "Sign up"}</button>
        </div>

        <Link>Already have an account?</Link>/  Create a new account
      </form>


    </div>


  )
}
