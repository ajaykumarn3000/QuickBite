import React, { useState } from "react";
import Dashboard from "./Dashboard/Dashboard";
import ManageMenu from "./ManageMenu/ManageMenu";
import SideBar from "./SideBar/SideBar";

const AdminPage = () => {
  const [section, setSection] = useState(null);
  return (
    <div className="flex w-full h-full bg-slate-100">
      <SideBar setSection={setSection}/>
      {section === 1 && <Dashboard/>}
      {section === 2 && <ManageMenu/>}
    </div>
  );
};

export default AdminPage;
