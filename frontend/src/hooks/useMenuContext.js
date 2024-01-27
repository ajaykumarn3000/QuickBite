import { useContext } from "react";
import { menuContext } from "../context/menuContext";

export default function useMenuContext() {
  const context = useContext(menuContext);

  if (!context) {
    throw new Error("useMenuContext must be used within a MenuProvider");
  }

  return context;
}