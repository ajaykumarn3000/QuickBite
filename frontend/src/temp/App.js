import React, { useState } from "react";
import "./styles.css";

function App() {
  const [signIn, toggle] = useState(false);

  return (
    <div className="UserAuth">
      <div className={`Register ${!signIn ? "Active" : ""}`}>
        <form>
          <h1>Register</h1>
          <input type="email" placeholder="Email" name="email" />
          <input type="password" placeholder="Password" name="password" />
          <button className="btn" type="submit">
            Register
          </button>
        </form>
      </div>
      <div className={`Login ${!signIn ? "Active" : ""}`}>
        <form>
          <h1>Login</h1>
          <input type="number" placeholder="PID" name="pid" />
          <input type="password" placeholder="Password" name="password" />
          <button className="btn" type="submit">
            Login
          </button>
        </form>
      </div>
      <div className={`OverlayContainer ${!signIn ? "Active" : ""}`}>
        <div className={`Overlay ${!signIn ? "Active" : ""}`}>
          <div className={`Left OverlayPanel ${!signIn ? "Active" : ""}`}>
            <h1>Login</h1>
            <p>
              To keep connected with us please login with your personal info
            </p>
            <button
              className="GhostButton"
              onClick={(e) => {
                toggle(!signIn);
              }}
            >
              SignIn
            </button>
          </div>
          <div className={`Right OverlayPanel ${!signIn ? "Active" : ""}`}>
            <h2>Register</h2>
            <p>Enter your personal details and start journey with us</p>
            <button
              className="GhostButton"
              onClick={(e) => {
                toggle(!signIn);
              }}
            >
              SignUp
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
