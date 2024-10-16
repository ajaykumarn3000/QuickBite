import { useState } from "react";
import MenuCard from "./MenuCard";
import Editor from "./Editor/Editor";
import clsx from "clsx";
import { useMenuContext } from "../context/menuContext";


const Menu = ({ open }) => {
  console.log("MENU");
  const [onMenu, setOnMenu] = useState(true);
  const { menu } = useMenuContext();

  return (
    <>
      <div className="flex h-full grow bg-white shadow">
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
              {menu.map(
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
              {/* {[
                1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 33, 35,
              ].map((item, index) => (
                <MenuCard
                  quantity={item}
                  name={"Cheese Burger"}
                  src={randomSrc()}
                  key={index}
                />
              ))} */}
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 xl:grid-cols-5 mt-4 gap-4">
              {menu.map(
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
      </div>
      <Editor/>
    </>
  );
};

export default Menu;
