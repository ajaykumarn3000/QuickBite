import requests
from src.setup import SERVER_URL
import json


def getCart(token: str):
    response = requests.get(
        f"{SERVER_URL}/user/api/cart",
        headers={"Authorization": f"Bearer {token}"},
    )
    if response.ok:
        data = response.json()
        for item in data:
            item["total"] = item["price"] * item["quantity"]
        return data
    return None
