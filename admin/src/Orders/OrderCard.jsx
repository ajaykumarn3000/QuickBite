import React from "react";
import { serveOrder } from "../controller/menuController";

const OrderCard = ({ data, setRefresh }) => {
  const handleClick = () => {
    serveOrder(data.user_id);
    setRefresh((prev) => !prev);
  };
  return (
    <div className="rounded-xl shadow-none transition-all hover:shadow border p-2 flex flex-col gap-1 relative hover:scale-105 active:scale-95 min-w-52">
      <h2 className="text-xl font-semibold">{data.user_id}</h2>
      <hr />
      <div className="">
        {data.items.map((item) => (
          <div key={item.item_id} className="flex justify-between">
            <p>{item.item_name}</p>
            <p>{item.item_quantity}</p>
          </div>
        ))}
      </div>
      <button
        className="mt-2 bg-gray-100 rounded py-1 px-3"
        onClick={handleClick}
      >
        SERVE
      </button>
    </div>
  );
};

export default OrderCard;
