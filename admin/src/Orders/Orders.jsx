import React from "react";
import OrderCard from "./OrderCard";
import { getAllOrders } from "../controller/menuController";

const Orders = () => {
  const [orders, setOrders] = React.useState([]);
  const [refresh, setRefresh] = React.useState(false);

  React.useEffect(() => {
    getAllOrders().then((data) => {
      setOrders(data);
    });
  }, [refresh]);

  return (
    <div className="flex h-full grow bg-white shadow">
      <div className="p-4 overflow-auto">
        <h1 className="text-xl font-semibold">Orders</h1>
        <div className="mt-4 w-full flex flex-wrap gap-4">
          {orders &&
            orders.map((order) => (
              <OrderCard
                key={order.user_id}
                data={order}
                setRefresh={setRefresh}
              />
            ))}
        </div>
      </div>
    </div>
  );
};

export default Orders;
