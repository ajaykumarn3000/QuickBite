import React from 'react'
import SideBarBtn from './SideBarBtn'

const SideBar = ({setSection}) => {
  return (
    <div className='bg-white m-2 rounded shadow'>
      <SideBarBtn title={"Dashboard"} onClick={() => setSection(1)}/>
      <SideBarBtn title={"Manage Menu"} onClick={() => setSection(2)}/>
      <SideBarBtn title={"Manage User"} onClick={() => setSection(3)}/>
      <SideBarBtn title={"Manage Order"} onClick={() => setSection(4)}/>
    </div>
  )
}

export default SideBar