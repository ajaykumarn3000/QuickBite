import React, { useEffect, useState } from "react";
import useUserContext from "../../hooks/useUserContext";
import {
  addToCart,
  removeFromCart,
  deleteFromCart,
} from "../../controllers/cartController";
import useCartContext from "../../hooks/useCartContext";
import useMenuContext from "../../hooks/useMenuContext";

const CartItem = React.memo(({ icon, name, id, quantity }) => {
  const {  dispatch: menuDispatch } = useMenuContext();
  useEffect(() => {
    menuDispatch({ type: "SET_SELECTED", payload: { id: id } });
  }, [id, menuDispatch]);
  const [hover, setHover] = useState(false);
  const { user } = useUserContext();
  const { cart, dispatch } = useCartContext();
  return (
    <div
      onMouseEnter={() => {
        setHover(true);
      }}
      onMouseLeave={() => {
        setHover(false);
      }}
      className={`CartItems relative flex p-2 transition-colors ${
        hover ? "bg-accent-200" : "bg-white"
      }`}
    >
      <img
        src={icon || "chicken-noodles.jpg"}
        alt={name}
        className="object-cente object-cover aspect-video max-w-40 rounded-lg shadow"
      />
      <div className="grow my-1 ml-3 flex flex-col justify-evenly">
        <p
          className={`text-center font-semibold text-xl transition-all ${
            hover ? "scale-110 text-gray-800" : "text-gray-500"
          }`}
        >
          {name}
        </p>
        <div className="flex justify-center items-center w-full">
          <button
            className="mx-2 flex items-center"
            onClick={() => {
              removeFromCart(user.token, id)
                .then((res) => {
                  console.log(res);
                  if (cart.find((item) => item.id === id).quantity === 1) {
                    dispatch({ type: "REMOVE_ITEM", payload: id });
                    menuDispatch({ type: "REMOVE_SELECTED", payload: { id: id } })
                  } else {
                    dispatch({ type: "DECREMENT_ITEM", payload: id });
                  }
                })
                .catch((err) => {
                  console.log(err);
                });
            }}
          >
            <span
              className={`material-symbols-rounded text-2xl rounded-full border-2  leading-none ${
                hover
                  ? "border-gray-800 text-gray-700"
                  : "border-gray-500 text-gray-500"
              }`}
            >
              remove
            </span>
          </button>
          <p
            className={`border-2 rounded-lg  font-bold px-5 cursor-default ${
              hover
                ? "border-gray-700 text-gray-700"
                : "border-gray-500 text-gray-500"
            }`}
          >
            {quantity}
          </p>
          <button
            className="mx-2 flex items-center"
            onClick={() => {
              addToCart(user.token, id)
                .then((res) => {
                  console.log(res);
                  dispatch({ type: "INCREMENT_ITEM", payload: id });
                })
                .catch((err) => {
                  console.log(err);
                });
            }}
          >
            <span
              className={`material-symbols-rounded text-2xl rounded-full border-2  leading-none ${
                hover
                  ? "border-gray-800 text-gray-700"
                  : "border-gray-500 text-gray-500"
              }`}
            >
              add
            </span>
          </button>
        </div>
      </div>
      <button
        className="m-1 absolute top-0 left-0"
        onClick={() => {
          deleteFromCart(user.token, id)
            .then((res) => {
              console.log(res);
              dispatch({ type: "REMOVE_ITEM", payload: id });
              menuDispatch({ type: "REMOVE_SELECTED", payload: { id: id } })
            })
            .catch((err) => {
              console.log(err);
            });
        }}
      >
        <span
          className={`material-symbols-rounded text-xl rounded-full bg-white/100 text-red-500 font-semibold leading-none ${
            hover
              ? "border-gray-800 text-gray-700"
              : "border-gray-500 text-gray-500"
          }`}
        >
          close
        </span>
      </button>
    </div>
  );
});

export default CartItem;
