import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import React from "react";
import useUserContext from "../hooks/useUserContext";
// User
import UserDashboard from "./Dashboard";
import Auth from "./Authentication/Auth";

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
            path="/auth"
            element={!user ? <Auth /> : <Navigate to="/" />}
          />

          {/* Default */}
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
