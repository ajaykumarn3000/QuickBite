import { SERVER_URL } from "../setup";

const sendOTP = async ({
  email,
  setEmailError,
  passcode,
  setPasscodeError,
  setShowOtp,
  setError,
  setLoading,
}) => {
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

const verifyOTP = async ({
  email,
  otp,
  setOtpError,
  setShowOtp,
  setError,
  dispatch,
}) => {
  try {
    const res = await fetch(SERVER_URL + "/user/auth/verify", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email, otp: otp }),
    });
    const data = await res.json();
    if (res.ok) {
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

const login = async ({
  pid,
  passcode,
  setPidError,
  setPasscodeError,
  setError,
  dispatch,
}) => {
  try {
    const res = await fetch(SERVER_URL + "/user/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ uid: pid, passcode: passcode }),
    });
    const data = await res.json();
    if (res.ok) {
      dispatch({ type: "LOGIN", payload: data.token });
    } else {
      if (data.detail.from === "uid") {
        setPidError(true);
      } else if (data.detail.from === "passcode") {
        setPasscodeError(true);
      }
      setError(data.detail.message);
    }
  } catch (e) {
    console.log(e);
    setError(e.message);
  }
};

export { sendOTP, verifyOTP, login };