from os import environ
from controller.otp import OTP
from models.Users import User, find_id, user_exists, id_exists, correct_passcode
from fastapi import APIRouter, Request
from controller.token import create_access_token, verify_access_token

router = APIRouter(
    prefix="/user/auth",
)

# TODO: Instead of returning message in case of errors, Throw HTTPException along with status code and detail

user_instance = OTP()

EMAIL_ID = environ.get('ADMIN_MAIL')
PASSWORD_ID = environ.get('PASSWORD')


@router.get('/')
def check_connection() -> None:
    """To check connection"""
    print("Checking successful")


@router.post('/register')
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
    # TODO: Add name of user from excel workbook
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


@router.post('/verify')
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
        return {"token": create_access_token(data={"user_type": "user", "uid": str(result["uid"])})}
    else:
        print(result["message"])
        return {
            "message": result["message"]
        }


@router.post('/login')
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
            return {"token": create_access_token(data={"user_type": "user", "uid": str(data["uid"])})}
        else:
            print('Incorrect password')
            return {
                "message": "Incorrect Password"
            }
