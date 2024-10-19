import React, { useState } from "react";
import useUserContext from "../../hooks/useUserContext";
import { useNavigate } from "react-router-dom";

const Dropdown = () => {
  const [showDropdown, setShowDropdown] = useState(false);
  const { dispatch } = useUserContext();
  const navigate = useNavigate();

  const onLogout = () => {
    dispatch({ type: "LOGOUT" });
  };

  return (
    <div className="Dropdown relative">
      <button
        onClick={() => {
          setShowDropdown((prevValue) => !prevValue);
        }}
        className="flex hover:text-accent-600 active:bg-gray-200"
      >
        <span className="material-symbols-rounded">menu</span>
      </button>
      <div
        className={`DropdownMenu w-32 text-sm text-[0.925rem] text-gray-500 font-semibold bg-white rounded shadow-[0_0_3px_rgba(0,0,0,0.4)] tracking-widest absolute top-full right-0 ${
          showDropdown ? "block" : "hidden"
        }`}
      >
        <button
          className="flex items-center w-full py-1 px-2 hover:text-amber-500"
          onClick={() => navigate("/orders")}
        >
          <span className="material-symbols-rounded mr-2">list_alt</span> My
          Order
        </button>
        <hr />
        <button className="flex items-center w-full py-1 px-2 hover:text-amber-500">
          <span className="material-symbols-rounded mr-2">settings</span>{" "}
          Setting
        </button>
        <hr />
        <button
          className="flex items-center w-full py-1 px-2  hover:text-red-500"
          onClick={onLogout}
        >
          <span className="material-symbols-rounded mr-2">logout</span> Logout
        </button>
      </div>
    </div>
  );
};

export default Dropdown;
