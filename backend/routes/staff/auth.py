# -*- coding: utf-8 -*-
from os import environ
from controller.staff_otp import OTP
from models.Staff import staff_exists, correct_passcode, Staff
from fastapi import FastAPI, Request, APIRouter, status, HTTPException

# FastAPI app router
router = APIRouter(prefix="/staff/auth")

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
        print('Staff already registered')
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Staff already registered",
        )
        # return {
        #     "message": "User already registered"
        # }
    else:
        user_data = {
            "email": email,
            "passcode": passcode,
        }
        user_instance.user_data.append(user_data)
        # The otp is to be sent to the admin for staff registration
        await user_instance.send_otp(email=email)
        return {
            "message": "OTP Successfully Sent"
        }


@router.post('/verify')
async def verify_email(request: Request) -> dict:
    data = await request.json()
    result = user_instance.verify_otp(otp=data['otp'], email=data["email"])
    new_user = Staff(email=result["email"], passcode=result["passcode"])
    new_user.save()
    return {"message": "Staff Successfully Verified"}


@router.post('/login')
async def login(request: Request) -> dict:
    data = await request.json()
    email, passcode = data['email'], data['passcode']
    if staff_exists(email=email):
        if correct_passcode(email=email, passcode=passcode):
            return {"message": "Login Successful"}
        else:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Incorrect password",
            )
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Email not registered",
        )
