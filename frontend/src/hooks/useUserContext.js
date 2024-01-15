import { useContext } from "react";
import { userContext } from "../context/userContext";

export default function useUserContext() {
  const context = useContext(userContext);

  if (!context) {
    throw new Error("useUserContext must be used within a UserProvider");
  }

  return context;
}
