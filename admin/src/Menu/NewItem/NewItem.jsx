import React, { useState } from "react";
import clsx from "clsx";
import InputLabel, { inputStyle } from "../../component/InputLabel";
import { FOOD_TYPES } from "../../setup";
import QuantityButton from "./../../component/QuantityButton";
import { addMenuItem } from "../../controller/menuController";
import { useMenuContext } from "../../context/menuContext";

const NewItem = () => {
  const {setCurrentItem, setRefresh} = useMenuContext();
  const [details, setDetails] = useState({
    name: "",
    price: 0,
    src: "",
    type: "",
    quantity: 0,
  });

  const handleChange = (e) => {
    setDetails({ ...details, [e.target.name]: e.target.value });
  };


  const handleConfirm = () => {
    addMenuItem(details).then(()=> {
      setRefresh((prev) => !prev);
      setCurrentItem(details);
      setDetails({ name: "", price: 0, src: "", type: "", quantity: 0 });
    })
  }
  return (
    <div className="py-4 px-4 max-w-72 min-w-72 bg-white">
      <div className=" flex flex-col items-end gap-2">
        <div className="flex justify-between w-full">
          <h1 className="text-xl font-semibold ">Item Details</h1>
        </div>
        <div className="relative aspect-video w-full">
          <img
            src={details.src}
            alt=""
            className="rounded object-cover aspect-video"
          />
          <div
            className={clsx(
              "absolute inset-0 transition-opacity bg-black/40 rounded flex items-center justify-center opacity-0",
              "opacity-100"
            )}
          >
            <input
              type="text"
              value={details.src}
              onChange={handleChange}
              name="src"
              className="w-full bg-transparent text-white border-white border-2 rounded-md px-1.5 py-0.5 m-2"
            />
          </div>
        </div>
        <div className="flex flex-col gap-4 w-full mt-2">
          <InputLabel title={"name"} htmlFor="item-name">
            <input
              type="text"
              name="name"
              id="item-name"
              value={details?.name}
              onChange={handleChange}
              className={inputStyle(false)}
            />
          </InputLabel>
          <InputLabel title={"type"} htmlFor="item-type">
            <select
              name="type"
              id="item-type"
              value={details?.type}
              onChange={handleChange}
              className={clsx(inputStyle(false), "disabled:opacity-100")}
            >
              {FOOD_TYPES.map((type, index) => (
                <option key={index} value={type}>
                  {type}
                </option>
              ))}
            </select>
          </InputLabel>

          <InputLabel title={"price"} htmlFor="item-price">
            <input
              type="number"
              name="price"
              value={details?.price}
              onChange={handleChange}
              id="item-price"
              className={inputStyle(false)}
            />
          </InputLabel>
        </div>
      </div>
      <div className="flex flex-col w-full mt-4 gap-2">
      <h1 className="text-xl font-semibold">Quantity Control</h1>
      <div className="grid grid-cols-[1fr_0.7fr] gap-y-2 gap-x-4">
        <div className="grid grid-cols-3 gap-2">
          {[1, 2, 5, 10, 15, 20].map((item, index) => (
            <QuantityButton
              key={index}
              onClick={() => setDetails((prev) => ({...prev, quantity: prev.quantity + item}))}
              quantity={item}
              add
            />
          ))}
          {[1, 2, 5, 10, 15, 20].map((item, index) => (
            <QuantityButton
              key={index}
              onClick={() => setDetails((prev) => ({...prev, quantity: prev.quantity - item}))}
              quantity={item}
            />
          ))}
        </div>
        <div className="grow flex flex-col gap-2 items-center">
          
          <InputLabel title="Quantity" htmlFor="total">
            <input
              type="number"
              name="quantity"
              value={details?.quantity}
              onChange={handleChange}
              className={clsx(inputStyle, "w-20 text-xl py-2 text-center")}
            />
          </InputLabel>
          
        </div>
       
      </div>
      <div className="flex gap-2">
        <button
          className="border-[1.5px] border-slate-600 rounded px-2"
          onClick={() => setDetails({ name: "", price: 0, src: "", type: "", quantity: 0 })}
        >
          Discard
        </button>
        <button
          className="bg-orange-400 text-white px-3 py-1 grow"
          onClick={handleConfirm}
        >
          ADD
        </button>
      </div>
    </div>
    </div>
  );
};

export default NewItem;
