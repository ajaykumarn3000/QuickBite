import React, { useState } from "react";
import { startTouch, moveTouch } from "./swipe.js";
import { SERVER_URL } from "../../../setup.js";
import useUserContext from "../../../hooks/useUserContext.js";

const Register = ({ login, setLogin }) => {
  const [email, setEmail] = useState("");
  const [emailError, setEmailError] = useState(false);

  const [passcode, setPasscode] = useState("");
  const [passcodeError, setPasscodeError] = useState(false);

  const [otp, setOtp] = useState("");
  const [showOtp, setShowOtp] = useState(false);
  const [otpError, setOtpError] = useState(false);

  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);
  const { dispatch } = useUserContext();

  const sendOTP = async (e) => {
    let domain;
    if (email.includes("@student.sfit.ac.in")) {
      domain = "student";
    } else if (email.includes("@sfit.ac.in")) {
      domain = "others";
    } else {
      setEmailError(true);
      setError("Please provide SFIT email");
      setLoading(false);
      return;
    }
    try {
      const res = await fetch(SERVER_URL + "/user/auth/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json", // Set the Content-Type header
        },
        body: JSON.stringify({
          username: email.split("@")[0],
          passcode: passcode,
          user_type: domain,
        }),
      });
      const data = await res.json();
      if (!res.ok) {
        console.log(data);
        if (data.detail.from === "email") {
          setEmailError(true);
        } else if (data.detail.from === "passcode") {
          setPasscodeError(true);
        }
        setError(data.detail.message);
      } else {
        setShowOtp(true);
      }
    } catch (e) {
      console.log(e);
      setError(e.message);
    }
  };

  const verifyOTP = async (e) => {
    try {
      const res = await fetch(SERVER_URL + "/user/auth/verify", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: email, otp: otp }),
      });
      const data = await res.json();
      if (res.ok) {
        console.log(data);
        dispatch({ type: "LOGIN", payload: data.token });
      } else {
        if (data.detail.from === "otp") {
          setOtpError(true);
        } else {
          setShowOtp(false);
        }
        setError(data.detail.message);
      }
    } catch (e) {
      console.log(e);
      setError(e.message);
    }
  };

  const handleSubmit = (e) => {
    setLoading(true);
    setError(null);
    setEmailError(false);
    setPasscodeError(false);
    setOtpError(false);
    e.preventDefault();

    if (showOtp) {
      if (otp !== "") {
        verifyOTP(e);
      } else {
        setOtpError(true);
      }
    } else {
      if (email && passcode) {
        sendOTP(e);
      } else {
        if (email === "") {
          setEmailError(true);
        }
        if (passcode === "") {
          setPasscodeError(true);
        }
        setLoading(false);
      }
    }
    setLoading(false);
  };

  return (
    <div className={`Register ${!login ? "Active" : ""}`}>
      <div className="AuthContainer">
        <form
          className="mobileBox  shadow-lg sm:shadow-none flex flex-col"
          onSubmit={(e) => {
            handleSubmit(e);
          }}
        >
          <h1 className="text-accent text-3xl mb-2 font-semibold">Register</h1>

          <div className="inputContainer">
            <div className={`email-password ${showOtp ? null : "Active"}`}>
              <input
                className={`text-gray-700 font-semibold tracking-wide text-lg border-solid boder-2 focus:bg-accent-100 focus:border-accent transition-colors duration-300 rounded-md ${
                  emailError
                    ? "border-red-500 bg-red-200"
                    : "border-white bg-background-200"
                }`}
                type="email"
                placeholder="SFIT Email"
                name="email"
                onChange={(e) => {
                  setEmail(e.target.value);
                }}
                value={email}
              />
              <input
                className={`text-gray-700 font-semibold tracking-wide text-lg border-solid boder-2 focus:bg-accent-100 focus:border-accent transition-colors duration-300 rounded-md ${
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
            </div>
            <div className={`otp ${showOtp ? "Active" : null}`}>
              <input
                className={`text-center tracking-widest text-gray-700 font-semibold text-lg bg-background-200 border-solid boder-2 focus:bg-accent-100 focus:border-accent transition-colors duration-300 rounded-md ${
                  otpError
                    ? "border-red-500 bg-red-200"
                    : "border-white bg-background-200"
                }`}
                type="number"
                placeholder="Enter OTP"
                name="otp"
                onChange={(e) => {
                  setOtp(e.target.value);
                }}
                value={otp}
              />
            </div>
          </div>

          {error && <p className="Error text-red-600 font-semibold">{error}</p>}
          <button
            className={`btn flex relative justify-center items-center self-center text-background font-bold rounded-lg transition-colors duration-300 border-1 mt-4 ${
              loading
                ? "bg-gray-400"
                : "bg-accent-400 shadow-md hover:bg-accent-450 active:bg-accent-500 active:shadow-none"
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
            <span className={loading ? "opacity-0" : ""}>
              {showOtp ? "Register" : "Send OTP"}
            </span>
          </button>
        </form>

        <div
          onTouchStart={startTouch}
          onTouchEnd={(e) => {
            if (moveTouch(e) === "left") {
              setLogin(true);
            }
          }}
          className="SwipeArea w-full py-4 text-gray-500 font-bold text-lg"
        >
          Already have a account?{" "}
          <span
            className="ml-4 text-accent-600"
            onClick={() => {
              setLogin(true);
            }}
          >
            Login
          </span>
        </div>
      </div>
    </div>
  );
};

export default Register;
