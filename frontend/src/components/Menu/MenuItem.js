import React from "react";
import PriceTag from "../../elements/Tags/PriceTag";
import StockTag from "../../elements/Tags/StockTag";
import { addToCart } from "../../controllers/cartController";
import useUserContext from "../../hooks/useUserContext";
import useCartContext from "../../hooks/useCartContext";

const MenuItem = (({ img, name, price, quantity, selected, id, type }) => {
  const { user } = useUserContext();
  const { cart, dispatch } = useCartContext();
  return (
    <div
      onClick={() => {
        console.log("id:" + id + "FoodItem clicked");
        addToCart(user.token, id)
          .then((res) => {
            if (cart.find((item) => item.id === id)) {
              dispatch({ type: "INCREMENT_ITEM", payload: id });
            } else {
              dispatch({
                type: "ADD_ITEM",
                payload: {
                  icon: img,
                  id: id,
                  name: name,
                  price: price,
                  quantity: 1,
                },
              });
            }
            console.log(res);
          })
          .catch((err) => {
            console.log(err);
          });
      }}
      className={
        "FoodItem h-fit max-w-40 m-2 relative rounded-lg bg-white shadow" +
        (selected ? " border-[3px] border-amber-500 shadow-md" : "")
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
});

export default MenuItem;
