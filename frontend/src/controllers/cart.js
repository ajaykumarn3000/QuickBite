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

const addToCart = async (id, token) => {
  console.log("id:" + id + "addToCart clicked");
  try {
    const res = await fetch(SERVER_URL + "/user/api/cart/add/" + id, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`,
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

export { getCart, addToCart };