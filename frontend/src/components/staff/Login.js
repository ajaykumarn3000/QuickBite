import React, { useState } from "react";
import { Link } from "react-router-dom";

import TextInput from "../../elements/TextInput";
import EmailInput from "../../elements/EmailInput";

import useStaffContext from "../../hooks/useStaffContext";

function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const { dispatch } = useStaffContext();
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (email && password) {
      try {
        const res = await fetch("http://127.0.0.1:5000/staff/auth/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            email: email,
            passcode: password,
          }),
        });
        const data = await res.json();
        if (res.ok) {
          dispatch({ type: "LOGIN", payload: data });
        } else {
          console.log(data);
          setError(data.detail);
        }
      } catch (err) {
        console.log(err);
        setError("Something went wrong");
      }
    }

    setPassword("");
    setEmail("");
  };

  return (
    <div className="Register h-full flex flex-col justify-center items-center self-center hover:cursor-default px-3">
      <h2 className="text-center text-3xl mb-2 text-gray-600 font-semibold">
        Login in <span className="text-amber-500 ">QuickBite</span>
      </h2>
      <form
        className="bg-white p-3 m-2 max-w-full shadow-md rounded"
        onSubmit={handleSubmit}
      >
        <EmailInput name="email" label="Email" hooks={{ email, setEmail }} />
        <TextInput
          type="password"
          name="password"
          label="Password"
          hooks={{ password, setPassword }}
        />
        <button
          className="w-full font-semibold bg-amber-200 p-1 text-lg my-2 text-center text-gray-700 hover:bg-amber-300 hover:text-gray-800 active:bg-amber-500 active:text-white shadow active:shadow-none transition-colors rounded"
          type="submit"
        >
          Login
        </button>
      </form>
      <span className="flex w-full sm:max-w-[40%] justify-around text-md">
        <p>Already have a account?</p>{" "}
        <Link to="/staff/register" className="text-amber-500 font-semibold">
          Register
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

export default Login;
