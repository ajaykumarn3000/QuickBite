import { SERVER_URL } from "../setup";

const getMenu = async (token) => {
  try {
    const res = await fetch(SERVER_URL + "/kitchen/menu", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    const data = await res.json();
    if (res.ok) {
      data.forEach((element) => {
        element.selected = false;
      });
      return data;
    } else {
    }
  } catch (err) {
    console.log(err);
  }
};

export { getMenu };
