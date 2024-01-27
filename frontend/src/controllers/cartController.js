import { SERVER_URL } from "../setup";

const getCart = async (token) => {
  try {
    const res = await fetch(SERVER_URL + "/user/api/cart", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    const data = await res.json();
    if (res.ok) {
      return data;
    } else {
      console.log(data);
    }
  } catch (err) {
    console.log(err);
  }
};

const addToCart = async (token, id) => {
  console.log("id:" + id + "addToCart clicked");
  try {
    const res = await fetch(SERVER_URL + "/user/api/cart/add/" + id, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ item_id: id }),
    });
    const data = await res.json();
    if (res.ok) {
      console.log(data);
    } else {
      console.log(data);
    }
  } catch (e) {
    console.log(e);
  }
};

const removeFromCart = async (token, id) => {
  console.log("id:" + id + "RemoveFromCart clicked");
  try {
    const res = await fetch(SERVER_URL + "/user/api/cart/remove/" + id, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ item_id: id }),
    });
    const data = await res.json();
    if (res.ok) {
      console.log(data);
    } else {
      console.log(data);
    }
  } catch (e) {
    console.log(e);
  }
};

const deleteFromCart = async (token, id) => {
  console.log("id:" + id + "DeleteFromCart clicked");
  try {
    const res = await fetch(SERVER_URL + "/user/api/cart/delete/" + id, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({ item_id: id }),
    });
    const data = await res.json();
    if (res.ok) {
      console.log(data);
    } else {
      console.log(data);
    }
  } catch (e) {
    console.log(e);
  }
};

export { getCart, addToCart, removeFromCart, deleteFromCart };
