import React, { useState } from "react";
import { startTouch, moveTouch } from "./swipe.js";
import useUserContext from "../../hooks/useUserContext.js";
import { login as userLogin } from "../../controllers/authController.js";

const Login = ({ login, setLogin }) => {
  const [pid, setPid] = useState("");
  const [pidError, setPidError] = useState(false);

  const [passcode, setPasscode] = useState("");
  const [passcodeError, setPasscodeError] = useState(false);

  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const { dispatch } = useUserContext();

  const handleSubmit = (e) => {
    setLoading(true);
    setError(null);
    setPidError(false);
    setPasscodeError(false);
    e.preventDefault();
    if (pid && passcode) {
      userLogin({
        pid,
        passcode,
        setPidError,
        setPasscodeError,
        setError,
        dispatch,
      });
    } else {
      if (!pid) setPidError(true);
      if (!passcode) setPasscodeError(true);
    }
    setLoading(false);
  };

  return (
    <div className={`Login ${!login ? "Active" : ""}`}>
      <div className="AuthContainer">
        <form
          className="mobileBox shadow-lg sm:shadow-none flex flex-col"
          onSubmit={(e) => {
            handleSubmit(e);
          }}
        >
          <h1 className="text-primary text-3xl mb-2 font-semibold">Login</h1>

          <input
            className={`text-gray-700 font-semibold tracking-wider text-lg border-solid boder-2 focus:bg-primary-100 focus:border-primary transition-colors duration-300 rounded-md ${
              pidError
                ? "border-red-500 bg-red-200"
                : "border-white bg-background-200"
            }`}
            type="number"
            name="pid"
            placeholder="PID"
            onChange={(e) => {
              setPid(e.target.value);
            }}
            value={pid}
          />
          <input
            className={`text-gray-700 font-semibold tracking-wide text-lg border-solid boder-2 focus:bg-primary-100 focus:border-primary transition-colors duration-300 rounded-md ${
              passcodeError
                ? "border-red-500 bg-red-200"
                : "border-white bg-background-200"
            }`}
            type="password"
            placeholder="Password"
            name="password"
            onChange={(e) => {
              setPasscode(e.target.value);
            }}
            value={passcode}
          />
          {error && <p className="Error text-red-600 font-semibold">{error}</p>}

          <button
            className={`btn flex relative justify-center items-center self-center text-background font-bold rounded-lg transition-colors duration-300 border-1 mt-4 ${
              loading
                ? "bg-gray-400"
                : "bg-primary-400 shadow-md hover:bg-primary-450 active:bg-primary-500 active:shadow-none"
            }`}
            type="submit"
            disabled={loading}
          >
            {loading && (
              <div className="absolute bottom-1/2 right-1/2 transform translate-x-1/2 translate-y-1/2">
                <span className="animate-spin material-symbols-rounded">
                  progress_activity
                </span>
              </div>
            )}
            <span className={loading ? "opacity-0" : ""}>Login</span>
          </button>
        </form>

        <div
          onTouchStart={startTouch}
          onTouchEnd={(e) => {
            if (moveTouch(e) === "right") {
              setLogin(false);
            }
          }}
          className="SwipeArea w-full py-4 text-gray-500 font-bold text-lg"
        >
          New to QuickBite?{" "}
          <span
            className="ml-4 text-primary-500"
            onClick={() => {
              setLogin(false);
            }}
          >
            Register
          </span>
        </div>
      </div>
    </div>
  );
};

export default Login;
