import React from "react";
import MenuItem from "./MenuItem";
// import useUserContext from "../../hooks/useUserContext";

// const getMenu = async (token) => {
//   try {
//     const res = await fetch(SERVER_URL + "/kitchen/menu", {
//       headers: {
//         Authorization: `Token ${token}`,
//       },
//     });
//     const data = await res.json();
//     if (res.ok) {
//       return data;
//     } else {
//       console.log(data);
//     }
//   } catch (err) {
//     console.log(err);
//   }
// };

const Menu = () => {
  // const [menu, setMenu] = useState([]);
  // useEffect(() => {
  //   getMenu(user.token).then((data) => {
  //     setMenu(data);
  //   });
  // }, [user.token]);
  return (
    <div className="Menu grow flex flex-wrap justify-evenly px-2 overflow-y-scroll">
      {/* {menu.map((item) => (
        <FoodItem
          key={item.item_id}
          id={item.item_id}
          img={"chicken-noodles.jpg"}
          name={item.item_name}
          price={item.item_price}
          quantity={item.item_quantity}
          type={item.item_type}
          selected={false}
        />
      ))} */}
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
      <MenuItem
        img="chicken-noodles.jpg"
        name="Chicken Noodles"
        price="34"
        quantity="14"
      />
    </div>
  );
};

export default Menu;
