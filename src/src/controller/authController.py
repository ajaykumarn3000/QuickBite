import requests
from src.setup import SERVER_URL
import json
from src.state import AuthState

def register(data: dict):
    data["user_type"] = "student"
    # some code
    response = requests.post(f"{SERVER_URL}/user/auth/register", data=json.dumps(data))
    if response.ok:
        return True
    print(response.json())
    return False

def verify_otp(data: dict):
    response = requests.post(f"{SERVER_URL}/user/auth/verify", data=json.dumps(data))
    if response.ok:
        return response.json()["token"]
    print(response.json())
    return ""

def login(data: dict):
    response = requests.post(f"{SERVER_URL}/user/auth/login", data=json.dumps(data))
    if response.ok:
        return response.json()["token"]
    print(response.json())
    return ""