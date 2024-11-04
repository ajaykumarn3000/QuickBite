import { useEffect, useState } from "react";
import MenuCard from "./MenuCard";
import Editor from "./Editor/Editor";
import clsx from "clsx";
import { useMenuContext } from "../context/menuContext";
import AddIcon from "@mui/icons-material/Add";
import NewItem from "./NewItem/NewItem";

const Menu = ({ open }) => {
  console.log("MENU");
  const [onMenu, setOnMenu] = useState(true);
  const { menu, currentItem } = useMenuContext();
  const [newItem, setNewItem] = useState(false);

  useEffect(() => {
    if (currentItem) {
      setNewItem(false);
    }
  }, [currentItem]);

  return (
    <>
      <div className="flex h-full grow bg-white shadow relative">
        <div className="p-4 overflow-auto">
          <h1
            className="cursor-pointer select-none"
            onClick={() => setOnMenu((prev) => !prev)}
          >
            <span
              className={clsx(
                "transition-all",
                onMenu && "text-xl font-semibold ease-in",
                !onMenu && "text-sm delay-150 ease-out"
              )}
            >
              On Menu
            </span>
            {" / "}
            <span
              className={clsx(
                "transition-all",
                !onMenu && "text-xl font-semibold ease-in",
                onMenu && "text-sm delay-150 ease-out"
              )}
            >
              Off Menu
            </span>
          </h1>
          {onMenu ? (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 2xl:grid-cols-5 mt-4 gap-4">
              {menu &&
                menu.map(
                  (
                    {
                      item_id,
                      item_name,
                      item_price,
                      item_quantity,
                      item_type,
                      item_icon,
                    },
                    index
                  ) =>
                    item_quantity > 0 && (
                      <MenuCard
                        id={item_id}
                        name={item_name}
                        price={item_price}
                        quantity={item_quantity}
                        type={item_type}
                        src={item_icon}
                        key={index}
                      />
                    )
                )}
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 xl:grid-cols-5 mt-4 gap-4">
              {menu &&
                menu.map(
                  (
                    {
                      item_id,
                      item_name,
                      item_price,
                      item_quantity,
                      item_type,
                      item_icon,
                    },
                    index
                  ) =>
                    item_quantity === 0 && (
                      <MenuCard
                        id={item_id}
                        name={item_name}
                        price={item_price}
                        quantity={item_quantity}
                        type={item_type}
                        src={item_icon}
                        key={index}
                        disabled
                      />
                    )
                )}
            </div>
          )}
        </div>
        <button
          className="absolute bottom-4 right-4 h-12 w-12 rounded-full bg-white shadow border flex justify-center items-center transition-transform hover:scale-105 active:scale-95"
          onClick={() => setNewItem(true)}
        >
          <AddIcon className="text-black text-lg font-semibold" />
        </button>
      </div>
      {newItem ? <NewItem /> : <Editor />}
    </>
  );
};

export default Menu;
