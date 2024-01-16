import { useContext } from "react";
import { staffContext } from "../context/staffContext";

export default function useStaffContext() {
  const context = useContext(staffContext);

  if (!context) {
    throw new Error("useStaffContext must be used within a StaffProvider");
  }

  return context;
}
