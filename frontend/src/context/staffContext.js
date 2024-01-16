import { createContext, useReducer } from "react";

const staffContext = createContext();

const staffReducer = (state, action) => {
  switch (action.type) {
    case "LOGIN":
      localStorage.setItem("staff", JSON.stringify(action.payload));
      return { staff: action.payload };
    case "LOGOUT":
      localStorage.removeItem("staff");
      return { staff: null };
    default:
      return state;
  }
};

const StaffProvider = ({ children }) => {
  // TODO Change this to true to test the login page
  const prevStaff = localStorage.getItem("staff") ? JSON.parse(localStorage.getItem("staff")) : null
  const [ state, dispatch ] = useReducer(staffReducer, { staff: prevStaff});

  console.log("StaffContext state:",state);

  return (
    <staffContext.Provider value={{ ...state, dispatch }}>
      {children}
    </staffContext.Provider>
  );
};

export { staffContext, StaffProvider };