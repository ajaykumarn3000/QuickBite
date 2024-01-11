import React, { useState } from "react";
import { Link } from "react-router-dom";

import TextInput from "../elements/TextInput";
import EmailInput from "../elements/EmailInput";
import NumberInput from "../elements/NumberInput";

function Register() {
  const [email, setEmail] = useState("");
  const [domain, setDomain] = useState("@student.sfit.ac.in");
  const [pid, setPid] = useState();
  const [password, setPassword] = useState("");
  // const [confirmPassword, setConfirmPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    // Form Logic

    setEmail("");
    setDomain("@student.sfit.ac.in");
    setPassword("");
    setPid("");
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
        <EmailInput
          name="email"
          label="Email"
          hooks={{ email, setEmail, domain, setDomain }}
        />
        <NumberInput name="pid" label="PID" hooks={{ pid, setPid }} />
        <TextInput
          type="password"
          name="password"
          label="Password"
          hooks={{ password, setPassword }}
        />
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
        <Link to="/login" className="text-amber-500 font-semibold">
          Login
        </Link>
      </span>
    </div>
  );
}

export default Register;
