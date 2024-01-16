import React, { useState } from "react";
import { Link } from "react-router-dom";

import TextInput from "../../elements/TextInput";
import EmailInput from "../../elements/EmailInput";
import NumberInput from "../../elements/NumberInput";

import useUserContext from "../../hooks/useUserContext";

function Register() {
  const [email, setEmail] = useState("");
  const [domain, setDomain] = useState("@student.sfit.ac.in");
  // const [pid, setPid] = useState("");
  const [password, setPassword] = useState("");
  const [otp, setOtp] = useState("");
  const [viewOtp, setViewOtp] = useState(false);
  const { dispatch } = useUserContext();
  const [error, setError] = useState("");
  // const [confirmPassword, setConfirmPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!viewOtp) {
      if (email && password) {
        try {
          const res = await fetch("http://127.0.0.1:5000/user/auth/register", {
            method: "POST",
            headers: {
              "Content-Type": "application/json", // Set the Content-Type header
            },
            body: JSON.stringify({
              username: email,
              passcode: password,
              user_type: domain === "@student.sfit.ac.in" ? "student" : "other",
            }),
          });

          if (res.ok) {
            setViewOtp(true);
            setError("");
          } else {
            const data = await res.json();
            setError(data.detail);
            console.log(data);
          }
        } catch (err) {
          console.log(err);
          setError("Something went wrong");
        }
      }
    } else {
      if (otp) {
        try {
          const res = await fetch("http://127.0.0.1:5000/user/auth/verify", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              email: email + domain,
              otp,
            }),
          });
          const data = await res.json();
          if (res.ok) {
            console.log(data);
            setViewOtp(false);
            setError("");
            dispatch({ type: "LOGIN", payload: data });
          } else {
            setError(data.detail);
            console.log(data);
          }
        } catch (err) {
          console.log(err);
          setError("Something went wrong");
        }

        setEmail("");
        setDomain("@student.sfit.ac.in");
        setPassword("");
        // setPid("");
        setOtp("");
        setViewOtp(false);
      }
    }
  };

  return (
    <div className="Register h-full flex flex-col justify-center items-center self-center hover:cursor-default px-3">
      <h2 className="text-center text-3xl mb-2 text-gray-600 font-semibold">
        Register to <span className="text-amber-500 ">QuickBite</span>
      </h2>
      <form
        className="bg-white p-3 m-2 max-w-full shadow-md rounded"
        onSubmit={handleSubmit}
      >
        {!viewOtp && (
          <>
            <EmailInput
              name="email"
              label="Email"
              hooks={{ email, setEmail, domain, setDomain }}
            />
            {/* <NumberInput name="pid" label="PID" hooks={{ pid, setPid }} /> */}
            <TextInput
              type="password"
              name="password"
              label="Password"
              hooks={{ password, setPassword }}
            />
          </>
        )}
        {viewOtp && (
          <NumberInput name="otp" label="OTP" hooks={{ otp, setOtp }} />
        )}
        {/* <TextInput
          type="password"
          name="confirmPassword"
          label="Confirm Password"
          hooks={{confirmPassword, setConfirmPassword}}
        /> */}
        <button
          className="w-full font-semibold bg-amber-200 p-1 text-lg my-2 text-center text-gray-700 hover:bg-amber-300 hover:text-gray-800 active:bg-amber-500 active:text-white shadow active:shadow-none transition-colors rounded"
          type="submit"
        >
          Register
        </button>
      </form>
      <span className="flex w-full sm:max-w-[40%] justify-around text-md">
        <p>Already have a account?</p>{" "}
        <Link to="/user/login" className="text-amber-500 font-semibold">
          Login
        </Link>
      </span>
      {error && (
        <p className="text-pink-700 font-medium text-md tracking-wide">
          {error}
        </p>
      )}
    </div>
  );
}

export default Register;
