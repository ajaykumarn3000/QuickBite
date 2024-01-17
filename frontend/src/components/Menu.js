import React from "react";
import FoodItem from "./FoodItem";

const Menu = () => {
  return (
    <div className="Menu flex flex-wrap justify-evenly">
      <FoodItem img="chicken-noodles.jpg" name="Chicken Noodles" price="34" quantity="14" selected={true}/>
      <FoodItem img="chicken-noodles.jpg" name="Chicken Noodles" price="34" quantity="14"/>
      <FoodItem img="chicken-noodles.jpg" name="Chicken Noodles" price="34" quantity="14"/>
      <FoodItem img="chicken-noodles.jpg" name="Chicken Noodles" price="34" quantity="14"/>
      <FoodItem img="chicken-noodles.jpg" name="Chicken Noodles" price="34" quantity="14"/>
      <FoodItem img="chicken-noodles.jpg" name="Chicken Noodles" price="34" quantity="14"/>
      <FoodItem img="chicken-noodles.jpg" name="Chicken Noodles" price="34" quantity="14"/>
      <FoodItem img="chicken-noodles.jpg" name="Chicken Noodles" price="34" quantity="14"/>
      <FoodItem img="chicken-noodles.jpg" name="Chicken Noodles" price="34" quantity="14"/>
      <FoodItem img="chicken-noodles.jpg" name="Chicken Noodles" price="34" quantity="14"/>
      <FoodItem img="chicken-noodles.jpg" name="Chicken Noodles" price="34" quantity="14"/>
      <FoodItem img="chicken-noodles.jpg" name="Chicken Noodles" price="34" quantity="14"/>
    </div>
  );
};

export default Menu;
