import React from "react";
import OrderInfo from "./OrderInfo";

const Order = ({ order }) => {
  const { successful, time, date, orderList } = order;
  return (
    <div className="Order flex rounded-md overflow-hidden shadow-md">
      <div
        className={`p-2 bg-white flex gap-4 ${!successful ? "min-w-72" : ""}`}
      >
        {!successful && (
          <div className="OrderCode text-center ml-2 flex flex-col justify-center">
            <img
              src="https://www.pngall.com/wp-content/uploads/2/QR-Code-PNG-HD-Image.png"
              alt=""
              className="max-w-20 max-h-20"
            />
            <p className="font-bold text-sm ">220177</p>
          </div>
        )}
        <OrderInfo orderList={orderList} />
      </div>
      <p
        style={{ writingMode: "vertical-lr", transform: "rotate(180deg)" }}
        className={`flex gap-2 text-sm font-semibold text-gray-500 px-1 py-2 ${
          !successful ? "bg-accent-100" : "bg-primary-200"
        }`}
      >
        {" "}
        <p>{time}</p>
        <p>{date}</p>
      </p>
    </div>
  );
};

export default Order;
