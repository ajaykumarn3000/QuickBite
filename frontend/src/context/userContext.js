import { createContext, useReducer } from "react";

const userContext = createContext();

const userReducer = (state, action) => {
  switch (action.type) {
    case "LOGIN":

      localStorage.setItem("user", JSON.stringify({token: action.payload}));
      return { user: {token: action.payload} };
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

  return (
    <userContext.Provider value={{ ...state, dispatch }}>
      {children}
    </userContext.Provider>
  );
};

export { userContext, UserProvider };
