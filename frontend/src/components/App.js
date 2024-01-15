import { BrowserRouter, Routes, Route } from "react-router-dom";
import React from "react";
import Home from "./Home";
import Register from "./Register";
import Login from "./Login";
import useUserContext from "../hooks/useUserContext";

function App() {
  const { user } = useUserContext();
  return (
    <div className="App h-dvh bg-gray-100">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={user ? <Home /> : <Login />} />
          <Route
            path="/user/register"
            element={user ? <Home /> : <Register />}
          />
          <Route path="/user/login" element={user ? <Home /> : <Login />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
