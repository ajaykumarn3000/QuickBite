import requests
from src.setup import SERVER_URL
import json


def getMenu(token: str):
    # some code
    response = requests.get(
        f"{SERVER_URL}/kitchen/menu",
        headers={"Authorization": f"Bearer {token}"},
    )
    if response.ok:
        return response.json()
    print(response.json())
    return None
