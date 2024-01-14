# -*- coding: utf-8 -*-
from os import environ
from controller.alt_otp import OTP
from models.Users import User, find_id, user_exists, id_exists, correct_passcode
from fastapi import FastAPI
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


@app.get('/register')
def register():
    """Function to be called when the user wants to register"""
    username = 'kevinxaviernadar'
    passcode = 'kxn_2004'
    user_type = 'student'
    email = (
        f'{username}@student.sfit.ac.in'
        if user_type == 'student'
        else f'{username}@sfit.ac.in'
    )
    found_id: list[int] = find_id(email=email)
    if not found_id:
        print('Email not found')
    else:
        if user_exists(email=email):
            print('User already registered')
        else:
            user_instance.uid = found_id[0]
            user_instance.passcode = passcode
            user_instance.send_otp(email=email)
            requests.get('http://127.0.0.1:8000/verify')


@app.get('/verify')
def verify_email():
    otp = input('Enter the otp: ')
    if user_instance.verify_otp(otp):
        print('Email verified')
        new_user = User(
            uid=user_instance.uid,
            email=user_instance.email,
            passcode=user_instance.passcode
        )
        new_user.save()
        print('User successfully verified')
    else:
        print('OTP is incorrect')


@app.get('/login')
def login():
    if not id_exists(uid=221078):
        print('This user is not registered')
    else:
        if correct_passcode(uid=221079, passcode='kxn_2004'):
            print('Login successful')
        else:
            print('Incorrect password')
