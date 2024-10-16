import React, { useState, useEffect } from "react";
import EditIcon from "@mui/icons-material/Edit";
import InputLabel, { inputStyle } from "../../component/InputLabel";
import clsx from "clsx";
import ModeEditRoundedIcon from "@mui/icons-material/ModeEditRounded";
import { useMenuContext } from "../../context/menuContext";
// import { FOOD_TYPES } from "../../setup";
import { editMenuItem } from "../../controller/menuController";

const ItemDetails = () => {
  console.log("ITEM DETAILS");
  const { currentItem, setCurrentItem, setRefresh } = useMenuContext();
  const [itemEdit, setItemEdit] = useState(currentItem);
  const [editing, setEditing] = useState(false);

  useEffect(() => {
    setEditing(false);
    setItemEdit(currentItem);
  }, [currentItem]);

  const handleChange = (e) => {
    setItemEdit({ ...itemEdit, [e.target.name]: e.target.value });
  };

  const handleSave = () => {
    setEditing(false);
    editMenuItem({
      id: currentItem?.id,
      name: itemEdit.name,
      price: itemEdit.price,
      quantity: currentItem?.quantity,
    }).then(() => {setRefresh((prev) => !prev);
      setCurrentItem((prev) => ({ ...prev, name: itemEdit.name, price: itemEdit.price }));
    });
  };

  return (
    <div className=" flex flex-col items-end gap-2">
      <div className="flex justify-between w-full">
        <h1 className="text-xl font-semibold ">Item Details</h1>
        {editing ? (
          <div className="flex gap-2">
            <button
              onClick={() => {
                setItemEdit(currentItem);
                setEditing(false);
              }}
              className="px-1 shadow rounded border-black border-[1.5px]"
            >
              cancel
            </button>
            <button
              onClick={handleSave}
              className="shadow bg-green-500 text-white px-2 rounded"
            >
              Save
            </button>
          </div>
        ) : (
          <button
            onClick={() => setEditing(true)}
            className="transition-colors rounded text-black flex font-medium items-center justify-center gap-0.5 w-fit px-1"
          >
            <ModeEditRoundedIcon fontSize="small" className="text-black" /> Edit
          </button>
        )}
      </div>
      <div className="relative">
        <img
          src={itemEdit?.src}
          alt=""
          className="rounded object-cover aspect-video"
        />

        <div
          className={clsx(
            "absolute inset-0 transition-opacity bg-black/40 rounded flex items-center justify-center opacity-0",
            editing && "opacity-100"
          )}
        >
          <span className="cursor-pointer hover:bg-slate-200 hover:text-black text-slate-200 border-[1.5px] px-2 text-sm rounded-full flex items-center gap-1">
            <EditIcon fontSize="xs" /> Change Image
          </span>
        </div>
      </div>
      <div className="flex flex-col gap-4 w-full mt-2">
        <InputLabel title={"name"} htmlFor="item-name" disabled={!editing}>
          <input
            type="text"
            name="name"
            id="item-name"
            value={itemEdit?.name}
            onChange={handleChange}
            disabled={!editing}
            className={inputStyle(!editing)}
          />
        </InputLabel>
        {/* <InputLabel title={"type"} htmlFor="item-type" disabled={!editing}>
          <select
            name="type"
            id="item-type"
            value={itemEdit?.type}
            onChange={handleChange}
            className={clsx(inputStyle(!editing), "disabled:opacity-100")}
            disabled={!editing}
          >
            {FOOD_TYPES.map((type, index) => (
              <option key={index} value={type}>
                {type}
              </option>
            ))}
          </select>
        </InputLabel> */}

        <InputLabel title={"price"} htmlFor="item-price" disabled={!editing}>
          <input
            type="number"
            name="price"
            value={itemEdit?.price}
            onChange={handleChange}
            id="item-price"
            disabled={!editing}
            className={inputStyle(!editing)}
          />
        </InputLabel>
      </div>
    </div>
  );
};

export default ItemDetails;
