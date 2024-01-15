import { createContext, useReducer } from "react";

const userContext = createContext();

const userReducer = (state, action) => {
  switch (action.type) {
    case "LOGIN":
      localStorage.setItem("user", JSON.stringify(action.payload));
      return { user: action.payload };
    case "LOGOUT":
      localStorage.removeItem("user");
      return { user: null };
    default:
      return state;
  }
};

const UserProvider = ({ children }) => {
  // TODO Change this to true to test the login page
  const prevUser = localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : null
  const [ state, dispatch ] = useReducer(userReducer, { user: prevUser});

  console.log("UserContext state:",state);

  return (
    <userContext.Provider value={{ ...state, dispatch }}>
      {children}
    </userContext.Provider>
  );
};

export { userContext, UserProvider };