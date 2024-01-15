# -*- coding: utf-8 -*-
from os import environ
from controller.staff_otp import OTP
from models.Staff import staff_exists, correct_passcode, Staff
from fastapi import FastAPI, Request, APIRouter

# FastAPI app router
router = APIRouter(prefix="/staff")

user_instance = OTP()

EMAIL_ID = environ.get('ADMIN_MAIL')
PASSWORD_ID = environ.get('PASSWORD')


@router.get('/')
def check_connection() -> dict:
    """To check connection"""
    return {"message": "Connection established"}


@router.post('/register')
async def register(request: Request) -> dict:
    """Function to be called when the user wants to register"""
    data = await request.json()
    print(data)
    email = data['email']
    passcode = data['passcode']

    if staff_exists(email=email):
        print('User already registered')
        return {
            "message": "User already registered"
        }
    else:
        user_data = {
            "email": email,
            "passcode": passcode,
        }
        user_instance.user_data.append(user_data)
        # The otp is to be sent to the admin for staff registration
        user_instance.send_otp(email=email)
        return {
            "message": "OTP Successfully Sent"
        }


@router.post('/verify')
async def verify_email(request: Request) -> dict:
    data = await request.json()
    result = user_instance.verify_otp(otp=data['otp'], email=data["email"])
    if not result["message"]:
        new_user = Staff(email=result["email"], passcode=result["passcode"])
        new_user.save()
        return {"message": "User Successfully Verified"}
    else:
        return {"message": result["message"]}


@router.post('/login')
async def login(request: Request) -> dict:
    data = await request.json()
    email, passcode = data['email'], data['passcode']
    if staff_exists(email=email):
        return (
            {"message": "Login Successful"}
            if correct_passcode(email=email, passcode=passcode)
            else {"message": "Incorrect password"}
        )
    else:
        return {"message": "Email not registered"}
