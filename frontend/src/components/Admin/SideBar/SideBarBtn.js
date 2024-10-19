import React from "react";

const SideBarBtn = ({ title, ...props }) => {
  return (
    <div className="text-center border-b-2 border-gray-500 font-semibold text-xl transition-all text-gray-500 p-2 px-4 hover:bg-accent-100 cursor-pointer" {...props}>
      {title}
    </div>
  );
};

export default SideBarBtn;
