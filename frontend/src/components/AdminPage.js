import React from "react";
import SideBar from "./Admin/SideBar";
import AdminDashboard from "./Admin/AdminDashboard";

const AdminPage = () => {
  return (
    <div className="flex w-full h-full bg-slate-100">
      <SideBar />
      <AdminDashboard />
    </div>
  );
};

export default AdminPage;
