import { createContext, useReducer } from "react";

const menuContext = createContext();

const menuReducer = (state, action) => {
  switch (action.type) {
    case "SET_MENU":
      return action.payload;
    case "SET_SELECTED":
      return state.map((item) => {
        if (item.item_id === action.payload.id) {
          return { ...item, selected: true };
        }
        return item;
      });
    case "REMOVE_SELECTED":
      return state.map((item) => {
        if (item.item_id === action.payload.id) {
          return { ...item, selected: false };
        }
        return item;
      });

    default:
      return state;
  }
};

const MenuContextProvider = ({ children }) => {
  const [menu, dispatch] = useReducer(menuReducer, []);

  return (
    <menuContext.Provider value={{ menu, dispatch }}>
      {children}
    </menuContext.Provider>
  );
};

export { menuContext, MenuContextProvider };
