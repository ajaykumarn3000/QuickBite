import React, {useState} from "react";
import Navbar from "../Navbar";
import Menu from "./Menu";
import Cart from "./Cart/Cart";

function Dashboard() {
  const [showCart, setShowCart] = useState(false);
  return (
    <div className="UserDashboard flex flex-col h-full">
      <Navbar type="user" />
      <div className="flex grow overflow-y-auto relative sm:pb-2">
        <Menu />
        <Cart showCart={showCart} setShowCart={setShowCart}/>
      </div>
      <button className="ShowCartBtn" onClick={()=>{setShowCart(!showCart)}}>{showCart ? "Hide Cart": "Show Cart"}</button>
    </div>
  );
}
export default Dashboard;
