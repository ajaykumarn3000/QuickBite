import { SERVER_URL } from "../setup";

export const getMenu = async () => {
  try {
    const response = await fetch(`${SERVER_URL}/kitchen/menu`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    });
    if (response.ok) {
      const data = await response.json();
      return data;
    } else {
      throw new Error("Request failed");
    }
  } catch {
    console.error("Request failed");
  }
};

export const addMenuItem = async (item) => {
  try {
    const response = await fetch(`${SERVER_URL}/kitchen/menu/add`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: item.name,
        price: item.price,
        quantity: item.quantity,
        icon: item.src,
        category: item.type,
      }),
    });
    if (response.ok) {
      const data = await response.json();
      console.log(data);
      return data;
    } else {
      throw new Error("Request failed");
    }
  } catch {
    console.error("Request failed");
  }
};

export const editMenuItem = async (item) => {
  try {
    const response = await fetch(`${SERVER_URL}/kitchen/menu/edit/${item.id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        item_name: item.name,
        item_price: item.price,
        item_quantity: item.quantity,
      }),
    });
    if (response.ok) {
      const data = await response.json();
      console.log(data);
      return data;
    } else {
      throw new Error("Request failed");
    }
  } catch {
    console.error("Request failed");
  }
};

export const editItemQuantity = async (item) => {
  try {
    const response = await fetch(`${SERVER_URL}/kitchen/menu/edit/${item.id}`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        item_name: item.name,
        item_price: item.price,
        item_quantity: item.quantity,
      }),
    });
    if (response.ok) {
      const data = await response.json();
      console.log(data);
      return data;
    } else {
      throw new Error("Request failed");
    }
  } catch {
    console.error("Request failed");
  }
};
