import React from "react";
import PriceTag from "../elements/PriceTag";
import StockTag from "../elements/StockTag";

const FoodItem = ({img, name, price, quantity, selected}) => {
  return (
    <div className={"FoodItem grow max-w-40 m-2 relative rounded-lg bg-white shadow" + (selected ? " border-2 border-amber-500 shadow-md": "")}>
      <div className="absolute top-[-8px] left-[-8px]">
      <PriceTag price={price}/>
      </div>
      <div className="absolute top-[-5px] right-[-8px]">
      <StockTag quantity={quantity}/>
      </div>


      <div className="rounded-t-lg overflow-hidden">
        <img
          src={img}
          alt=""
          className="object-cente object-cover aspect-video"
        />
      </div>
      <h3 className="text-gray-600 font-semibold text-center">
        {name}
      </h3>
    </div>
  );
};

export default FoodItem;
