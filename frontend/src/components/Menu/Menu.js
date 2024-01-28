import React, { useEffect } from "react";
import MenuItem from "./MenuItem";
import useMenuContext from "../../hooks/useMenuContext";
import useUserContext from "../../hooks/useUserContext";
import { getMenu } from "../../controllers/menuController";
import useCartContext from "../../hooks/useCartContext";

const Menu = React.memo((() => {
  const { menu, dispatch } = useMenuContext();
  const { cart } = useCartContext();
  const { user } = useUserContext();
  useEffect(() => {
    getMenu(user.token)
      .then((data) => {
        data.forEach((element) => {
          element.selected = false;
        });
        dispatch({ type: "SET_MENU", payload: data });
        console.log(data)
      })
      .catch((err) => {
        console.log(err);
      });
  }, [user.token]);

  return (
    <div className="Menu grow flex flex-wrap justify-evenly px-2 overflow-y-scroll">
      {menu.map((item) => (
        <MenuItem
          key={item.item_id}
          id={item.item_id}
          img={item.item_icon || "chicken-noodles.jpg"}
          name={item.item_name}
          price={item.item_price}
          quantity={item.item_quantity}
          type={item.item_type}
          selected={item.selected}
        />
      ))}
    </div>
  );
}));

export default Menu;
