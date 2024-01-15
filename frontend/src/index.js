import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import App from "./components/App";

import "./index.css";
import { UserProvider } from "./context/userContext";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <UserProvider>
      <App />
    </UserProvider>
  </React.StrictMode>
);
