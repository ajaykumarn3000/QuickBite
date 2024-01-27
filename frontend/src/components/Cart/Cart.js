import React, { useEffect, useState } from "react";
import CartItem from "./CartItem";
import CartInfo from "./CartInfo";
import "./Cart.css";
import useCartContext from "../../hooks/useCartContext";
import useUserContext from "../../hooks/useUserContext";
import useMenuContext from "../../hooks/useMenuContext";
import { getCart } from "../../controllers/cartController";

const Cart = React.memo(({ showCart, setShowCart }) => {
  const { cart, dispatch } = useCartContext();
  const { menu } = useMenuContext();
  const { user } = useUserContext();
  useEffect(() => {
    getCart(user.token)
      .then((res) => {
        dispatch({ type: "SET_CART", payload: res });
      })
      .catch((err) => {
        console.log(err);
      });
  }, [user.token]);

  const [showInfo, setShowInfo] = useState(false);
  return (
    <div
      className={`Cart flex flex-col-reverse relative bg-white rounded-lg mr-2 shadow max-h-full right-0 bottom-0 sm:min-w-auto min-w-max h-full ${
        showCart ? "Active" : ""
      }`}
    >
      <div className="CartBtn">
        <p className="flex justify-between mx-4 my-2 font-semibold text-xl">
          <span>Total Amount: </span>
          <span>
            ₹{" "}
            {cart &&
              cart.reduce((total, item) => {
                return total + item.price * item.quantity;
              }, 0)}
          </span>
        </p>

        <div className="flex mx-4 my-2 font-bold text-2xl items-center">
          <button
            onClick={() => setShowInfo((prev) => !prev)}
            className="flex justify-center items-center w-11 h-11 border-2 text-accent transition-colors border-accent hover:bg-accent hover:text-white rounded-full font-black shadow"
          >
            {showInfo ? "X" : "i"}
          </button>
          <button className="grow bg-primary hover:bg-primary-450 transition-colors ml-2 py-2 rounded text-white shadow">
            CHECKOUT
          </button>
        </div>
      </div>

      <hr />

      <div
        className={`CartInfo overflow-y-scroll px-2 ${
          showInfo ? "Active" : ""
        }`}
      >
        {cart && cart.map((item) => <CartInfo key={item.id} {...item} />)}
      </div>

      <div
        className={`CartList overflow-y-scroll px-2 ${
          showInfo ? "" : "Active"
        }`}
      >
        {cart && cart.map((item) => <CartItem key={item.id} {...item} />)}
      </div>
    </div>
  );
});

export default Cart;
