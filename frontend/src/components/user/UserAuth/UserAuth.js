import React, { useState } from "react";
import "./styles.css";
import Register from "./Register";
import Login from "./Login";

const UserAuth = () => {
  const [login, setLogin] = useState(true);
  
  return (
    <div className="h-full flex justify-center items-center">
      <div className="UserAuth bg-background shadow-lg rounded-xl">
        <Register {...{ login, setLogin }} />
        <Login {...{ login, setLogin }} />
        <div className={`OverlayContainer ${!login ? "Active" : ""}`}>
          <div
            className={`Overlay ${!login ? "Active bg-accent" : "bg-primary"}`}
          >
            <div className={`Left OverlayPanel ${!login ? "Active" : ""}`}>
              <h2 className="font-bold text-3xl mb-3">Create a Account</h2>
              <h5>Enter your personal details and start journey with us</h5>
              <button
                className="GhostButton border-2 border-white px-8 py-2 rounded-full font-semibold hover:underline"
                onClick={(e) => {
                  setLogin(!login);
                }}
              >
                SignIn
              </button>
            </div>
            <div className={`Right OverlayPanel ${!login ? "Active" : ""}`}>
              <h2 className="font-bold text-3xl mb-3">Welcome Back!</h2>
              <h5>
                To keep connected with us please login with your personal info
              </h5>
              <button
                className="GhostButton border-2 border-white px-8 py-2 rounded-full font-semibold hover:underline"
                onClick={() => {
                  setLogin(!login);
                }}
              >
                Register
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default UserAuth;
