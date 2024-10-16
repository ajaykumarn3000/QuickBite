import clsx from "clsx";
import React from "react";
import { useMenuContext } from "../context/menuContext";

const MenuCard = ({ id, name, price, type, src, quantity, disabled }) => {

  console.log("MENU CARD")
  const {setCurrentItem} = useMenuContext();

  return (
    <div className="rounded-xl shadow-none transition-all hover:shadow border p-2 flex flex-col gap-1 cursor-pointer relative hover:scale-105 active:scale-95"
      onClick={()=>setCurrentItem({id, name, price, type, src, quantity})}
    >
      <img className="rounded-lg grow object-coverp aspect-video" src={src} alt="" />
      <p className="text-center text-sm">{name}</p>
      {!disabled && (
        <span
          className={clsx(
            "-top-2 -right-2 rounded-full py-0.5 px-1.5 absolute text-xs",
            [
              "border-[1.5px] bg-red-50 border-red-500 text-red-500",
              "border-[1.5px] bg-orange-50 border-orange-500 text-orange-500",
              "border-[1.5px] bg-yellow-50 border-yellow-500 text-yellow-500",
              "border-[1.5px] bg-green-50 border-green-500 text-green-500",
            ][Math.min(Math.floor(quantity / 5), 3)]
          )}
        >
          {quantity} left
        </span>
      )}
    </div>
  );
};

export default MenuCard;
