import { createContext, useContext, useEffect, useState } from "react";
import { getMenu } from "../controller/menuController";

const MenuContext = createContext();

export const MenuContextProvider = ({ children }) => {
  const [menu, setMenu] = useState([]);
  const [refresh, setRefresh] = useState(false);
  const [currentItem, setCurrentItem] = useState(null);
  useEffect(() => {
    getMenu().then((data) => {
      setMenu(data);
    });
  }, [refresh])
  return (
    <MenuContext.Provider value={{ menu, setMenu, currentItem, setCurrentItem, setRefresh }}>
      {children}
    </MenuContext.Provider>
  );
};

export const useMenuContext = () => {
  return useContext(MenuContext);
};
