import React from "react";
import useUserContext from "../../hooks/useUserContext";

const Logout = () => {
  const { dispatch } = useUserContext();
  const onClick = () => {
    dispatch({ type: "LOGOUT" });
  };
  return (
    <div className="Logout">
      <button
        className="logout 
        font-semibold mx-2 text-lg text-gray-400 w-fit 
        hover:text-white hover:text-red-600 transition-colors flex justify-center items-center"
        onClick={onClick}
      >
        <span className="material-symbols-rounded">logout</span>
      </button>
    </div>
  );
};

export default Logout;
