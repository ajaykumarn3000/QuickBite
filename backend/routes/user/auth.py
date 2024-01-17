# -*- coding: utf-8 -*-
import logging
from os import environ
from pydantic import BaseModel, EmailStr
from fastapi import APIRouter, status, HTTPException

from backend.controller.otp import OTP
from backend.controller.token import create_access_token
from backend.models.Users import User, find_id, user_exists, id_exists, correct_passcode

router = APIRouter(prefix="/user/auth")

user_instance = OTP()

EMAIL_ID = environ.get('ADMIN_MAIL')
PASSWORD_ID = environ.get('PASSWORD')


def logger_object():
    """Function to create a logger object to log the backend to the console"""
    logger = logging.getLogger(__name__)

    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


log = logger_object()


class UserRegisterRequest(BaseModel):
    """Request model for the register endpoint"""
    username: str
    passcode: str
    user_type: str


class VerifyEmailRequest(BaseModel):
    """Request model for the verify endpoint"""
    otp: str
    email: EmailStr


class UserLoginRequest(BaseModel):
    """Request model for the login endpoint"""
    uid: str
    passcode: str


class TokenResponse(BaseModel):
    """Response model for the token endpoint"""
    token: str


@router.get('/')
def check_connection():
    """To check connection"""
    log.info("Connection Established")
    return {"message": "Connection Established"}


@router.post('/register')
async def register(request: UserRegisterRequest):
    """
    Endpoint to register a new user and initiate the OTP (One-Time Password) verification process.

    This endpoint allows users to register by providing their username, chosen passcode,
    and user type. The email address is generated based on the username and user type.
    Upon successful registration, an OTP is sent to the user's email for verification.

    Parameters:
    - request (Request): FastAPI Request object containing user registration data in the request body.

    Request Body:
    - username (str): User's chosen username for registration.
    - passcode (str): User's chosen passcode for secure authentication.
    - user_type (str): User type, either "student" or another type.

    Returns:
    - Success (200): If the registration is successful, returns a message indicating the OTP is sent.
      Example:
      {
          "message": "OTP Successfully Sent"
      }

    - Raises:
      - HTTPException (status_code=404): If the generated email does not have a corresponding ID in the database.
        Example:
        {
            "detail": "Email does not found"
        }
      - HTTPException (status_code=406): If the user is already registered with the provided email.
        Example:
        {
            "detail": "User already registered"
        }

    Example Usage:
    - Used during the registration process to create a new user and initiate email verification.
    - OTP is crucial for completing the registration process.

    Security Considerations:
    - Ensure secure handling of user passcodes and email addresses.
    - Implement proper rate limiting to prevent abuse and protect against automated attacks.
    - Use HTTPS to encrypt data during transmission.

    Notes:
    - This endpoint assumes the use of an OTP system for secure email verification.
    - User information is stored temporarily in the user_instance for OTP validation.
    """

    email = (  # The domain of the email is different based on the type of user
        f'{request.username}@student.sfit.ac.in'  # Domain is student.sfit.ac.in
        if request.user_type == 'student'  # If the user type is student
        else f'{request.username}@sfit.ac.in'  # Otherwise it is sfit.ac.in
    )
    # Returns a list containing the ID of the email in the database if it exists
    found_id = find_id(email=email)
    if not found_id:  # If the email of the user is not in the student database
        log.info(f"Email: {email} not found in SE IT B Student Database")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found in SE IT B Student Database"
        )
    elif user_exists(email=email):  # If the user has already registered
        log.info(f"Email: {email} has already registered")
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=f"User has already registered",
        )
    else:  # If the user's email is in the student database and isn't registered
        # Add the user's data to the user_instance variable for otp verification
        user_instance.user_data.append(
            {
                "uid": found_id[0],
                "passcode": request.passcode,
                "email": email
            }
        )
        await user_instance.send_otp(email=email)  # Send OTP to user's email
        log.info(f"OTP sent to {email}")
        return {"message": "OTP sent to User"}


@router.post('/verify')
async def verify_email(request: VerifyEmailRequest):
    """
    Endpoint to verify a user's email using the provided OTP (One-Time Password).

    This endpoint is responsible for validating a user's email after they have
    received and entered the OTP sent during the registration process. Upon successful
    verification, the user's information is saved to the database, and an access token
    is generated for future secure interactions.

    Parameters:
    - request (Request): FastAPI Request object containing OTP and email data in the request body.

    Request Body:
    - otp (str): One-Time Password entered by the user for email verification.
    - email (str): User's email address for which the OTP was sent.

    Returns:
    - Success (200): If the email verification is successful, returns a JSON with an access token.
      Example:
      {
          "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3R5cGUiOiJ1c2VyIiwidWlkIjoiMTIzNDU2Nzg5MCIsImlhdCI6MTUxNjIzOTAyMn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
      }

    - Raises:
      - HTTPException (status_code=400): If the provided OTP is incorrect or expired.
        Example:
        {
            "detail": "Incorrect or expired OTP"
        }
      - HTTPException (status_code=500): If an unexpected error occurs during email verification.
        Example:
        {
            "detail": "Internal Server Error"
        }

    Example Usage:
    - Used during the registration process to verify the user's email.
    - Access tokens are crucial for subsequent secure interactions with the application.

    Security Considerations:
    - Implement secure handling of OTPs and ensure their one-time use.
    - Use HTTPS to encrypt data during transmission.
    - Implement proper rate limiting to prevent brute-force attacks.

    Notes:
    - This endpoint assumes the use of JWT (JSON Web Tokens) for secure access token generation.
    - User information is saved to the database upon successful email verification.
    """
    # Verify the OTP entered by the user and return the user's data, if correct
    result = user_instance.verify_otp(otp=request.otp, email=request.email)
    User(  # Create a user object with the user data and save it to the database
        uid=result["uid"],
        email=result["email"],
        passcode=result["passcode"]
    ).save()
    log.info(f"Email: {result['email']}'s uid is {result['uid']}")
    return {  # Return a JSON with an access token upon successful verification
        "Message": "User successfully verified",
        "token": create_access_token(
            data={"user_type": "user", "uid": str(result["uid"])}
        )
    }


@router.post('/login')
async def login(request: UserLoginRequest):
    """
    Authenticate a user by verifying the provided UID and passcode.

    This endpoint is responsible for authenticating users based on their unique
    user ID (UID) and passcode. Upon successful authentication, an access token is
    generated and returned, allowing the user to access protected resources.

    Parameters:
    - request (Request): FastAPI Request object containing user data in the request body.

    Request Body:
    - uid (str): User ID to be authenticated.
    - passcode (str): User's passcode for authentication.

    Returns:
    - Success (200): If the login is successful, returns a JSON with an access token.
      Example:
      {
          "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX3R5cGUiOiJ1c2VyIiwidWlkIjoiMTIzNDU2Nzg5MCIsImlhdCI6MTUxNjIzOTAyMn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
      }

    - Failure (404): If the user ID is not registered, returns HTTP 404 with an error message.
      Example:
      {
          "detail": "User not registered"
      }

    - Failure (406): If the provided passcode is incorrect, returns HTTP 406 with an error message.
      Example:
      {
          "detail": "Incorrect Password"
      }

    Raises:
    - HTTPException (status_code=404): If the user ID is not found in the database.
    - HTTPException (status_code=406): If the provided passcode does not match the stored passcode.

    Example Usage:
    - Used to authenticate a user during the login process.
    - Access tokens are crucial for subsequent secure interactions with the application.

    Security Considerations:
    - Ensure secure transmission of user credentials.
    - Implement proper rate limiting and account lockout mechanisms to prevent brute-force attacks.
    - Use HTTPS to encrypt data during transmission.

    Notes:
    - This endpoint assumes the use of JWT (JSON Web Tokens) for secure access token generation.
    - The user's passcode should be securely hashed and stored in the database.
    """
    if not id_exists(uid=request.uid):  # If the user has not registered yet
        log.info(f"PID: {request.uid} not registered")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not registered"
        )
    # Check if the provided passcode matches the stored passcode
    elif correct_passcode(uid=request.uid, passcode=request.passcode):
        # Generate an access token upon successful authentication
        access_token = create_access_token(
            data={"user_type": "user", "uid": str(request.uid)}
        )
        log.info(f"PID: {request.uid} has logged in")
        return {"message": "User has now logged in", "token": access_token}
    else:
        log.info(f"PID: {request.uid} has entered an incorrect password")
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Incorrect Password",
        )
