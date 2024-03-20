import React from "react";

const OrderInfo = ({ orderList }) => {
  return (
    <div className="OrderInfo w-full mx-2 flex flex-col justify-around">
      {orderList.map(({ id, name, quantity, price }) => {
        return (
          <p className="gap-8 flex justify-between font-medium text" key={id}>
            <span>
              {name} x {quantity}
            </span>
            <span>₹ {quantity * price}</span>
          </p>
        );
      })}
      <hr />
      <p className="gap-8 flex justify-between font-medium text text-lg">
        <span>Total:</span>
        <span>₹ {69420}</span>
      </p>
    </div>
  );
};

export default OrderInfo;
