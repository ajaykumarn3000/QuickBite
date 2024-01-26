import React from "react";
import { Link } from "react-router-dom";
import UserLogout from "./Authentication/Logout";

const Navbar = ({ type }) => {
  return (
    <div className="Navbar flex w-full justify-between items-center px-2 py-1 shadow bg-white mb-2">
      <Link
        to="/"
        className="text-amber-600 hover:text-amber-700 text-2xl font-semibold"
      >
        QuickBite
      </Link>
      {type === "user" && <UserLogout />}
    </div>
  );
};

export default Navbar;
