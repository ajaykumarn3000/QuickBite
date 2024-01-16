import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./components/App";

import "./index.css";
import { UserProvider } from "./context/userContext";
import { StaffProvider } from "./context/staffContext";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <UserProvider>
      <StaffProvider>
        <App />
      </StaffProvider>
    </UserProvider>
  </React.StrictMode>
);
