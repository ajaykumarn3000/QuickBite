// import { SERVER_URL } from "../setup";

const getMenu = async (token) => {
  try {
    const res = await fetch("https://quickbite-backend-r4mlunp2sa-el.a.run.app/ajay/kitchen/menu", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
    const data = await res.json();
    if (res.ok) {
      data.forEach(element => {
        element.selected = false;
      });
      return data;
    } else {
      console.log(data);
    }
  } catch (err) {
    console.log(err);
  }
};

export { getMenu };
