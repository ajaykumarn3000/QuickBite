import React from "react";
import useStaffContext from "../../hooks/useStaffContext";

const Logout = () => {
  const { dispatch } = useStaffContext();
  const onClick = () => {
    dispatch({ type: "LOGOUT" });
  };
  return (
    <div className="Logout">
      <button
        className="logout font-semibold mx-2 text-lg text-yellow-600 hover:text-white hover:bg-red-600 hover:border-red-600 transition-colors border-2 border-yellow-500 rounded px-2 pb-1"
        onClick={onClick}
      >
        Logout
      </button>
    </div>
  );
};

export default Logout;
