import {createContext, useReducer} from "react";

const menuContext = createContext();

const menuReducer = (state, action) => {
    switch (action.type) {
        case "SET_MENU":
            return action.payload;

        default:
            return state;
    }
}

const MenuContextProvider = ({children}) => {
  const [menu, dispatch] = useReducer(menuReducer, []);

  return (
      <menuContext.Provider value={{menu, dispatch}}>
          {children}
      </menuContext.Provider>
  );
}

export {menuContext, MenuContextProvider};
