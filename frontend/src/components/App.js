import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import React from "react";
import useUserContext from "../hooks/useUserContext";
import useStaffContext from "../hooks/useStaffContext";
// User
import UserDashboard from "./user/Dashboard";
// import Register from "./user/Register";
// import Login from "./user/Login";
import UserAuth from "./user/UserAuth/UserAuth";
// Staff
import StaffDashboard from "./staff/Dashboard";
import RegisterStaff from "./staff/Register";
import LoginStaff from "./staff/Login";

function App() {
  const { user } = useUserContext();
  const { staff } = useStaffContext();
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
            element={!user ? <UserAuth /> : <Navigate to="/" />}
          />

          {/* Staff */}
          <Route
            path="/staff"
            element={
              staff ? <StaffDashboard /> : <Navigate to="/staff/login" />
            }
          />
          <Route
            path="/staff/register"
            element={staff ? <Navigate to="/staff" /> : <RegisterStaff />}
          />
          <Route
            path="/staff/login"
            element={staff ? <Navigate to="/staff" /> : <LoginStaff />}
          />

          {/* Default */}
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
