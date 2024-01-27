import React from "react";

const PriceTag = ({ price }) => {
  return (
    <div className="PriceTag flex justify-center items-center relative w-9 h-9">
      <img src="pricetag.png" alt="" className="absolute w-9 h-9" />
      <h3 className="absolute text-white font-semibold text-sm">₹{price}</h3>
    </div>
  );
};

export default PriceTag;
