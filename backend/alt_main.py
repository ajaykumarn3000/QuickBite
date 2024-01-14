# -*- coding: utf-8 -*-
from os import environ
from controller.alt_otp import OTP
from models.Users import User, find_id, user_exists, id_exists, correct_passcode
from fastapi import FastAPI, Request
import requests

# FastAPI app
app = FastAPI()

user_instance = OTP()

EMAIL_ID = environ.get('ADMIN_MAIL')
PASSWORD_ID = environ.get('PASSWORD')


@app.get('/')
def check_connection() -> None:
    """To check connection"""
    print("Checking successful")


@app.post('/register')
async def register(request: Request):
    """Function to be called when the user wants to register"""
    data = await request.json()
    print(data)
    username = data['username']
    passcode = data['passcode']
    user_type = data['user_type']

    email = (
        f'{username}@student.sfit.ac.in'
        if user_type == 'student'
        else f'{username}@sfit.ac.in'
    )
    found_id: list[int] = find_id(email=email)
    if not found_id:
        print('Email not found')
        return {
            "message": "Email does not exist"
        }
    else:
        if user_exists(email=email):
            print('User already registered')
            return {
                "message": "User already registered"
            }
        else:
            user_data = {
                "uid": found_id[0],
                "passcode": passcode,
                "email": email
            }
            user_instance.user_data.append(user_data)
            user_instance.uid = found_id[0]
            user_instance.passcode = passcode
            print("Sending OTP")
            user_instance.send_otp(email=email)
            return {
                "message": "OTP Successfully Sent"
            }


@app.post('/verify')
async def verify_email(request: Request):
    data = await request.json()
    result = user_instance.verify_otp(otp=data['otp'], email=data["email"])
    if not result["message"]:
        print('Email verified')
        print(result)
        new_user = User(
            uid=result["uid"],
            email=result["email"],
            passcode=result["passcode"]
        )
        new_user.save()
        print('User successfully verified')
        return {
            "message": "User Successfully Verified"
        }
    else:
        print(result["message"])
        return {
            "message": result["message"]
        }


@app.post('/login')
async def login(request: Request):
    data = await request.json()
    uid = data['uid']
    passcode = data['passcode']
    if not id_exists(uid=uid):
        print('This user is not registered')
        return {
            "message": "User not registered"
        }
    else:
        if correct_passcode(uid=uid, passcode=passcode):
            print('Login successful')
            return {
                "message": "Login Successful"
            }
        else:
            print('Incorrect password')
            return {
                "message": "Incorrect Password"
            }
