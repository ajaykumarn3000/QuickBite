import React, { useState } from "react";
import Menu from "./Menu/Menu";
import Cart from "./Cart/Cart";
import { CartContextProvider } from "../context/cartContext";
import { MenuContextProvider } from "../context/menuContext";

const MenuAndCart = () => {
  const [showCart, setShowCart] = useState(false);
  return (
    <>
      <MenuContextProvider>
        <CartContextProvider>
          <div className="flex grow overflow-y-auto relative sm:pb-2">
            <Menu />
            <Cart showCart={showCart} setShowCart={setShowCart} />
          </div>
        </CartContextProvider>
      </MenuContextProvider>

      <button
        className="ShowCartBtn"
        onClick={() => {
          setShowCart((prev) => !prev);
        }}
      >
        {showCart ? "Hide Cart" : "Show Cart"}
      </button>
    </>
  );
};

export default MenuAndCart;
