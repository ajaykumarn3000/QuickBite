import React from "react";
import PriceTag from "../elements/PriceTag";
import StockTag from "../elements/StockTag";
// import { SERVER_URL } from "../../setup.js";

// const addToCart = async (id) => {
//   console.log("id:"+ id+"addToCart clicked");
//   try {
//     const res = await fetch(SERVER_URL + "/user/cart/add", {
//       method: "POST",
//       headers: { "Content-Type": "application/json" },
//       body: JSON.stringify({ item_id: id }),
//     });
//     const data = await res.json();
//     if (res.ok) {
//       console.log(data);
//     } else {
//       console.log(data);
//     }
//   } catch (e) {
//     console.log(e);
//   }
// }

const FoodItem = ({ img, name, price, quantity, selected, id, type }) => {
  return (
    <div
      onClick={() => {console.log("id:"+ id+"FoodItem clicked")}}
      className={
        "FoodItem h-fit max-w-40 m-2 relative rounded-lg bg-white shadow" +
        (selected ? " border-2 border-amber-500 shadow-md" : "")
      }
    >
      <div className="absolute top-[-8px] left-[-8px]">
        <PriceTag price={price} />
      </div>
      <div className="absolute top-[-5px] right-[-8px]">
        <StockTag quantity={quantity} />
      </div>

      <div className="rounded-t-lg overflow-hidden">
        <img
          src={img}
          alt=""
          className="object-cente object-cover aspect-video"
        />
      </div>
      <h3 className="text-gray-600 font-semibold text-center">{name}</h3>
    </div>
  );
};

export default FoodItem;
