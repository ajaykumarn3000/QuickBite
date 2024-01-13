import React, { useState } from "react";
import { Link } from "react-router-dom";

import TextInput from "../elements/TextInput";
import EmailInput from "../elements/EmailInput";
import NumberInput from "../elements/NumberInput";

function Register() {
  const [email, setEmail] = useState("");
  const [domain, setDomain] = useState("@student.sfit.ac.in");
  const [pid, setPid] = useState("");
  const [password, setPassword] = useState("");
  const [otp, setOtp] = useState("");
  const [viewOtp, setViewOtp] = useState(false);
  // const [confirmPassword, setConfirmPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!viewOtp) {
      if (email && pid && password) {
        try {
          const res = await fetch("http://localhost:5000/user/auth/register", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              // ? TODO: remove this
              email: email,
              // email: email + domain,
              pid,
              password,
            }),
          });
          if (res.ok) {
            setViewOtp(true);
          } else {
            const data = await res.json();
            console.log(data);
          }
          const data = await res.json();
        } catch (err) {
          console.log(err);
        }
      }
      setEmail("");
      setDomain("@student.sfit.ac.in");
      setPassword("");
      setPid("");
    } else {
      if (otp) {
        try {
          const res = await fetch("http://localhost:5000/user/auth/verify", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
              email: email + domain,
              otp
            }),
          });
          if (res.ok) {
            const data = await res.json();
            console.log(data, );

            setViewOtp(false);
            setEmail("Successfully Registered");
          } else {
            
            const data = await res.json();
            setEmail(data.message)
            console.log(data);
          }
        } catch (err) {
          console.log(err);
        }
      }
      // setEmail("");
      setDomain("@student.sfit.ac.in");
      setPassword("");
      setPid("");
      setOtp("");
      setViewOtp(false);
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
            <NumberInput name="pid" label="PID" hooks={{ pid, setPid }} />
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
    </div>
  );
}

export default Register;
