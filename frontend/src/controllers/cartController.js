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
    } else {
      console.log(data);
    }
  } catch (e) {
    console.log(e);
  }
};

// const payForCart = async (token, id) => {
//   if (!id) {
//     return;
//   }
//   try {
//     window.location.href = SERVER_URL + `/user/api/cart/checkout/${id}`;
//     // const res = await fetch(SERVER_URL + `/user/api/cart/checkout/${id}`, {
//     //   method: "GET",
//     //   headers: {
//     //     "Content-Type": "application/json",
//     //     Authorization: `Bearer ${token}`,
//     //   },
//     // });
//     // const data = await res.json();
//     // if (res.ok) {
//     //   console.log(String(data));
//     // } else {
//     //   console.log(data);
//     // }
//   } catch (e) {
//     console.log(e);
//   }
// };

const checkoutCart = async (token) => {
  console.log("Checkout clicked");
  try {
    const res = await fetch(SERVER_URL + "/user/api/cart/checkout", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
    });
    const data = await res.json();
    if (res.ok) {
      console.log(data);
      return data;
    } else {
      console.log(data);
    }
  } catch (e) {
    console.log(e);
  }
};

export { getCart, addToCart, removeFromCart, deleteFromCart, checkoutCart };
