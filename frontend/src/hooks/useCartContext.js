import { useContext } from "react";
import { cartContext } from "../context/cartContext";

export default function useCartContext() {
  const context = useContext(cartContext);

  if (!context) {
    throw new Error("useCartContext must be used within a CartProvider");
  }

  return context;
}