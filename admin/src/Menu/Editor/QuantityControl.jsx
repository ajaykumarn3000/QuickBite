import { useEffect, useState } from "react";
import QuantityButton from "../../component/QuantityButton";
import clsx from "clsx";
import AddIcon from "@mui/icons-material/Add";
import RemoveIcon from "@mui/icons-material/Remove";
import { SERVER_URL } from "../../setup";
import { useMenuContext } from "../../context/menuContext";
import InputLabel, { inputStyle } from "../../component/InputLabel";
import {
  deleteMenuItem,
  editItemQuantity,
} from "../../controller/menuController";

const QuantityControl = () => {
  console.log("QUANTITY CONTROL");
  // const [add, setAdd] = useState(true);
  const { currentItem, setRefresh, setCurrentItem } = useMenuContext();
  const [quantity, setQuantity] = useState(currentItem?.quantity);

  useEffect(() => {
    setQuantity(currentItem?.quantity);
    console.log("QUANTITY CONTROL useEffect", quantity);
  }, [currentItem]);

  const handleConfirm = () => {
    editItemQuantity({ id: currentItem?.id, quantity: quantity }).then(() => {
      setRefresh((prev) => !prev);
      setCurrentItem((prev) => ({ ...prev, quantity }));
    });
  };

  const handleDelete = () => {
    deleteMenuItem(currentItem?.id).then(() => {
      setRefresh((prev) => !prev);
      setCurrentItem(null);
    });
  };

  return (
    <div className="flex flex-col w-full mt-4 gap-2">
      <h1 className="text-xl font-semibold">Quantity Control</h1>
      <div className="grid grid-cols-[1fr_0.7fr] gap-y-2 gap-x-4">
        <div className="grid grid-cols-3 gap-2">
          {[1, 2, 5, 10, 15, 20].map((item, index) => (
            <QuantityButton
              key={index}
              onClick={() =>
                setQuantity((prev) => parseInt(prev) + parseInt(item))
              }
              quantity={item}
              add
            />
          ))}
          {[1, 2, 5, 10, 15, 20].map((item, index) => (
            <QuantityButton
              key={index}
              onClick={() => setQuantity((prev) => prev - item)}
              quantity={item}
            />
          ))}
        </div>
        <div className="grow flex flex-col gap-2 items-center">
          <div className="flex flex-col items-end">
            <div
              className={clsx(
                "w-14 h-14 rounded-lg flex flex-col justify-center items-center border-[1.5px] border-black",
                [
                  "border-[1.5px] bg-red-50 border-red-500 text-red-500",
                  "border-[1.5px] bg-orange-50 border-orange-500 text-orange-500",
                  "border-[1.5px] bg-yellow-50 border-yellow-500 text-yellow-500",
                  "border-[1.5px] bg-green-50 border-green-500 text-green-500",
                ][Math.min(Math.floor(currentItem?.quantity / 5), 3)]
              )}
            >
              <p className="font-semibold text-xl leading-6">
                {currentItem?.quantity}
              </p>
              <p className="text-xs leading-3 font-medium">in stock</p>
            </div>
            <div className="flex gap-0.5 px-1">
              <span>{quantity - currentItem?.quantity < 0 ? "-" : "+"}</span>
              <span>{Math.abs(quantity - currentItem?.quantity)}</span>
            </div>
          </div>
          <InputLabel title="Total" htmlFor="total">
            <input
              type="number"
              value={quantity}
              onChange={(e) => setQuantity(e.target.value)}
              className={clsx(inputStyle, "w-16 text-xl py-2 text-center")}
            />
          </InputLabel>
          {/* <button
            onClick={() => setAdd((prev) => !prev)}
            className="select-none h-6 aspect-square flex justify-center items-center bg-slate-100 border-[1.5px] rounded-full border-black font-semibold text-lg"
          >
            {add ? (
              <AddIcon fontSize="" className="font-black text-lg" />
            ) : (
              <RemoveIcon fontSize="" className="font-black text-lg" />
            )}
          </button> */}
          {/* <AddIcon fontSize="" className="font-black text-lg" /> */}
          {/* <div
            className={clsx(
              "w-14 h-14 rounded-lg flex justify-center items-center",
              "shadow bg-slate-100 "
            )}
          >
            <AddIcon fontSize="" className="font-black text-lg" /><p className="font-semibold text-xl leading-6">
              {currentItem?.quantity}
            </p>
          </div> */}
        </div>
        {/* <hr className=" col-span-2 border-black" />
        <div className="font-semibold flex items-end justify-end">TOTAL :</div>
        <div className="flex justify-center">
          <input
            type="number"
            value={quantity}
            onChange={(e) => setQuantity(e.target.value)}
            className="w-16 border-[1.5px] border-black outline-none rounded px-1 text-center"
          />
        </div>
        <hr className=" col-span-2 border-black" /> */}
      </div>
      <div className="flex gap-2">
        <button
          className="border-[1.5px] border-slate-600 rounded px-2"
          onClick={() => setQuantity(currentItem?.quantity)}
        >
          Discard
        </button>
        <button
          className="bg-orange-400 text-white px-3 py-1 grow"
          onClick={handleConfirm}
        >
          CONFIRM
        </button>
      </div>
      <button
        onClick={handleDelete}
        className="bg-red-500 text-white py-1 px-3 mt-4 "
      >
        DELETE
      </button>
    </div>
  );
};

export default QuantityControl;
