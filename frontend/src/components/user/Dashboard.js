import React from "react";
import Navbar from "../Navbar";
import Menu from "../Menu";

function Dashboard() {
  return (
    <div className="UserDashboard">
      <Navbar type="user"/>
      <Menu />
    </div>
  );
}
export default Dashboard;
