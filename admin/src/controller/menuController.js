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
        type: item.type,
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

export const deleteMenuItem = async (id) => {
  try {
    const response = await fetch(`${SERVER_URL}/kitchen/menu/delete/${id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
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

export const getAllOrders = async () => {
  try {
    const response = await fetch(`${SERVER_URL}/kitchen/orders`, {
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
  } catch (error) {
    console.error("Request failed");
  }
  // return [
  //   {
  //     user_id: 221077,
  //     items: [
  //       {
  //         item_id: 4,
  //         item_name: "Red Sauce Pasta",
  //         item_quantity: 5,
  //       },
  //       {
  //         item_id: 5,
  //         item_name: "Veg Thali",
  //         item_quantity: 1,
  //       },
  //       {
  //         item_id: 1,
  //         item_name: "Pav Bhaji",
  //         item_quantity: 2,
  //       },
  //     ],
  //   },
  //   {
  //     user_id: 221123,
  //     items: [
  //       {
  //         item_id: 5,
  //         item_name: "Veg Thali",
  //         item_quantity: 1,
  //       },
  //       {
  //         item_id: 8,
  //         item_name: "Kheema Pav",
  //         item_quantity: 1,
  //       },
  //       {
  //         item_id: 2,
  //         item_name: "Chole Bhature",
  //         item_quantity: 1,
  //       },
  //     ],
  //   },
  // ];
};

export const serveOrder = async (user_id) => {
  try {
    const response = await fetch(
      `${SERVER_URL}/kitchen/serve?user_id=${user_id}`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    if (response.ok) {
      const data = await response.json();
      console.log(data);
      return data;
    } else {
      throw new Error("Request failed");
    }
  } catch (error) {
    console.error("Request failed");
  }
};
