import { createContext, useReducer } from "react";

const menuContext = createContext();

const menuReducer = (state, action) => {
  switch (action.type) {
    case "SET_MENU":
      return action.payload;
    case "SET_SELECTED":
      console.log("id:" + action.payload.id + "FoodItem clicked");
      return state.map((item) => {
        if (item.item_id === action.payload.id) {
          return { ...item, selected: true };
        }
        return item;
      });
    case "REMOVE_SELECTED":
      console.warn("id:" + action.payload.id + "FoodItem clicked");
      return state.map((item) => {
        if (item.item_id === action.payload.id) {
          return { ...item, selected: false };
        }
        return item;
      });
      console.warn("State: ", state);
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
