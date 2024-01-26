import React, { useState } from "react";

const CartItem = ({ img, name, price, id, quantity, type }) => {
  const [hover, setHover] = useState(false);
  return (
    <div
      onMouseEnter={() => {
        setHover(true);
      }}
      onMouseLeave={() => {
        setHover(false);
      }}
      className={`CartItems flex p-2 transition-colors ${
        hover ? "bg-accent-200" : "bg-white"
      }`}
    >
      <img
        src={img}
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
          <button className="mx-2 flex items-center">
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
          <button className="mx-2 flex items-center">
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
    </div>
  );
};

export default CartItem;
