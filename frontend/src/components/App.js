import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import React from "react";
import useUserContext from "../hooks/useUserContext";
// User
import UserDashboard from "./UserDashboard";
import Auth from "./Authentication/Auth";
import AdminPage from "./Admin/AdminPage";
import OrdersPage from "./Orders/OrdersPage";

function App() {
  const { user } = useUserContext();
  return (
    <div className="App h-dvh bg-slate-100">
      <BrowserRouter>
        <Routes>
          {/* User */}
          <Route
            path="/"
            element={user ? <UserDashboard /> : <Navigate to="/auth" />}
          />
          <Route
            path="/orders"
            element={user ? <OrdersPage /> : <Navigate to="/auth" />}
          />
          <Route
            path="/auth"
            element={!user ? <Auth /> : <Navigate to="/" />}
          />
          <Route path="/admin" element={<AdminPage />} />

          {/* Default */}
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
