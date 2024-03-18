import React from "react";
import { Link } from "react-router-dom";
import Dropdown from "./Dropdown";

const Navbar = ({ type }) => {
  return (
    <div className="Navbar flex w-full justify-between items-center px-2 py-1 shadow bg-white mb-2">
      <Link
        to="/"
        className="text-primary-500 hover:text-primary-600 text-2xl font-semibold"
      >
        QuickBite
      </Link>
      {type === "user" && <Dropdown />}
    </div>
  );
};

export default Navbar;
