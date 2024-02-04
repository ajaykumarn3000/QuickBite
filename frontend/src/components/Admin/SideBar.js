import React from "react";

const SideBar = () => {
  return (
    <div className="SideBar w-64 bg-white m-2 rounded-lg shadow">
      <div className="p-2 pl-4 hover:bg-accent-100 border-b-2 border-slate-200 cursor-pointer">
        <p className="text-lg font-semibold text-gray-700 ">Dashboard</p>
      </div>
      <div className="p-2 pl-4 hover:bg-accent-100 border-b-2 border-slate-200 cursor-pointer">
        <p className="text-lg font-semibold text-gray-700 ">Manage Menu</p>
      </div>
      <div className="p-2 pl-4 hover:bg-accent-100 border-b-2 border-slate-200 cursor-pointer">
        <p className="text-lg font-semibold text-gray-700 ">Manage Staff</p>
      </div>
    </div>
  );
};

export default SideBar;
