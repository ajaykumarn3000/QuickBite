import { MenuContextProvider } from "./context/menuContext";
import Dashboard from "./Dashboard";
import Menu from "./Menu/Menu";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Orders from "./Orders/Orders";

function App() {
  console.log("APP");
  return (
    <div className="App h-dvh font-poppins">
      <MenuContextProvider>
        <BrowserRouter>
          <Dashboard>
            {/* <Menu/> */}
            <Routes>
              <Route path="/" element={<Menu />} />
              <Route path="/orders" element={<Orders />} />
            </Routes>
          </Dashboard>
        </BrowserRouter>
      </MenuContextProvider>
    </div>
  );
}

export default App;
