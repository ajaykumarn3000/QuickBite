import React from 'react'
import { Link } from 'react-router-dom'
import Logout from "./Logout"

const Navbar = () => {
  return (
    <div className='Navbar flex w-full justify-between items-center px-2 py-1 shadow bg-white mb-2'>
      <Link to="/" className='text-amber-600 hover:text-amber-700 text-2xl font-semibold'>QuickBite</Link>
      <Logout />
    </div>
  )
}

export default Navbar