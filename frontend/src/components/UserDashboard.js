import React, { useState } from "react";
import Navbar from "./Navbar/Navbar";
import MenuAndCart from "./MenuAndCart";

function UserDashboard() {
  return (
    <div className="UserDashboard flex flex-col h-full">
      <Navbar type="user" />
      <MenuAndCart />
    </div>
  );
}

export default UserDashboard;
