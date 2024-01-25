import React from "react";

const CartInfo = ({name, price, quantity}) => {
  return (
    <>
      <hr />
      <p className="flex justify-between font-medium text-lg my-2">
        <span>{quantity} x {name} (₹ {price})</span> <span>₹ {quantity*price}</span>
      </p>
    </>
  );
};

export default CartInfo;
