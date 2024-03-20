import React from "react";
import Navbar from "../Navbar/Navbar";
import Order from "./Order";

const OrdersPage = () => {
  const orders = [
    {
      successful: false,
      time: "10:45 AM",
      date: "20/01/24",
      orderList: [
        { id: 1, name: "Burger", quantity: 2, price: 100 },
        { id: 2, name: "Pizza", quantity: 1, price: 200 },
        { id: 3, name: "Pasta", quantity: 1, price: 150 },
      ],
    },
    {
      successful: false,
      time: "10:45 AM",
      date: "20/01/24",
      orderList: [
        { id: 1, name: "Burger", quantity: 2, price: 100 },
        { id: 2, name: "Pizza", quantity: 1, price: 200 },
        { id: 3, name: "Pasta", quantity: 1, price: 150 },
      ],
    },
    {
      successful: false,
      time: "10:45 AM",
      date: "20/01/24",
      orderList: [
        { id: 1, name: "Burger", quantity: 2, price: 100 },
        { id: 2, name: "Pizza", quantity: 1, price: 200 },
        { id: 3, name: "Pasta", quantity: 1, price: 150 },
      ],
    },
    {
      successful: true,
      time: "11:45 AM",
      date: "20/01/24",
      orderList: [
        { id: 1, name: "Burger", quantity: 2, price: 100 },
        { id: 2, name: "Pizza", quantity: 1, price: 200 },
        { id: 3, name: "Pasta", quantity: 1, price: 150 },
      ],
    },
    {
      successful: true,
      time: "11:45 AM",
      date: "20/01/24",
      orderList: [
        { id: 1, name: "Burger", quantity: 2, price: 100 },
        { id: 2, name: "Pizza", quantity: 1, price: 200 },
        { id: 3, name: "Pasta", quantity: 1, price: 150 },
      ],
    },
    {
      successful: true,
      time: "11:45 AM",
      date: "20/01/24",
      orderList: [
        { id: 1, name: "Burger", quantity: 2, price: 100 },
        { id: 2, name: "Pizza", quantity: 1, price: 200 },
        { id: 3, name: "Pasta", quantity: 1, price: 150 },
      ],
    },
    {
      successful: true,
      time: "12:45 AM",
      date: "20/01/24",
      orderList: [
        { id: 1, name: "Burger", quantity: 2, price: 100 },
        { id: 2, name: "Pizza", quantity: 1, price: 200 },
        { id: 3, name: "Pasta", quantity: 1, price: 150 },
        { id: 4, name: "Pasta", quantity: 1, price: 150 },
      ],
    },
  ];
  return (
    <div className="OrdersPage">
      <Navbar type="user" />
      <div className="Orders flex flex-wrap p-4 pt-2 gap-4">
        {orders.map((order, index) => (
          <Order order={order} key={index} />
        ))}
      </div>
    </div>
  );
};

export default OrdersPage;
