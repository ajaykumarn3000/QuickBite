import React from "react";

const StockTag = ({ quantity }) => {
  return (
    <div className="PriceTag flex justify-center items-center bg-green-500 px-1 rounded">
      <h3 className="text-white font-semibold text-sm">{quantity} left</h3>
    </div>
  );
};

export default StockTag;
