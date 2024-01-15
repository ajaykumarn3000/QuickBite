import { BrowserRouter, Routes, Route,Navigate } from "react-router-dom";
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
          <Route path="/" element={user ? <Home /> : <Navigate to="/user/login" />} />
          <Route
            path="/user/register"
            element={user ? <Navigate to="/" /> : <Register />}
          />
          <Route path="/user/login" element={user ? <Navigate to="/" /> : <Login />} />
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
