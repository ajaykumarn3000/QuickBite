# -*- coding: utf-8 -*-
import logging
import time
from datetime import datetime
from os import environ

from fastapi import HTTPException, status
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pyotp import TOTP, random_base32

from models.Users import get_name_by_email


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


# Mail configuration
mail_config = ConnectionConfig(
    MAIL_USERNAME=environ.get('ADMIN_MAIL'),
    MAIL_PASSWORD=environ.get('PASSWORD'),
    MAIL_FROM=environ.get('ADMIN_MAIL'),
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_SSL_TLS=False,
    MAIL_STARTTLS=True
)

# FastMail instance
fm = FastMail(mail_config)


class OTP:
    """
    Class for managing One-Time Password (OTP) functionality.

    Methods:
    - send_otp(email: str) -> dict: Sends an OTP to the specified email for user registration.

    Attributes:
    - user_data (List[dict]): List to store user data including email, OTP, and timestamp.

    Example Usage:
    - otp_instance = OTP()
    - otp_instance.send_otp(email="user@example.com")

    Security Considerations:
    - Ensure secure transmission of OTP.
    - Implement proper rate limiting for OTP requests.
    - Use HTTPS to encrypt data during transmission.

    Notes:
    - The OTP is generated using TOTP (Time-based One-Time Password) with a validity of 5 minutes.
    - The user_data attribute is used to store user-specific data during the OTP generation process.
    """

    def __init__(self):
        self.user_data = []
        self.sender_email = environ.get('ADMIN_MAIL')

    async def send_otp(self, email: str) -> dict:
        """
        Sends an OTP (One-Time Password) to the specified email for user registration.

        Parameters:
        - email (str): The email address to which the OTP will be sent.

        Returns:
        - Success (dict): If the email is sent successfully, returns a message indicating success.
          Example:
          {
              "message": "Email sent successfully"
          }

        Raises:
        - HTTPException (status_code=500): If an error occurs while sending the email.

        Example Usage:
        - Used to send an OTP to the user's email during the registration process.

        Security Considerations:
        - Ensure secure transmission of OTP.
        - Implement proper rate limiting for OTP requests.
        - Use HTTPS to encrypt data during transmission.

        Notes:
        - The OTP is generated using TOTP (Time-based One-Time Password) with a validity of 5 minutes.
        - The email contains a personalized HTML template with the user's name and OTP.
        - If the email sending fails, an HTTPException with status code 500 is raised.
        """
        name = get_name_by_email(email=email)
        otp = TOTP(random_base32()).now()
        html = f"""
        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <meta http-equiv="X-UA-Compatible" content="ie=edge" />
            <title>Static Template</title>

            <link
              href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap"
              rel="stylesheet"
            />
          </head>
          <body
            style="
              margin: 0;
              font-family: 'Poppins', sans-serif;
              background: #ffffff;
              font-size: 14px;
            "
          >
            <div
              style="
                max-width: 680px;
                margin: 0 auto;
                padding: 45px 30px 60px;
                background: #f4f7ff;
                background-image: url(https://archisketch-resources.s3.ap-northeast-2.amazonaws.com/vrstyler/1661497957196_595865/email-template-background-banner);
                background-repeat: no-repeat;
                background-size: 800px 452px;
                background-position: top center;
                font-size: 14px;
                color: #434343;
              "
            >
              <header>
                <table style="width: 100%;">
                  <tbody>
                    <tr style="height: 0;">
                      <td>
                        <img
                          alt=""
                          src="https://placeholderlogo.com/img/placeholder-logo-1.png"
                          height="170px"
                          width="250px"
                        />
                      </td>
                      <td style="text-align: right;">
                        <span
                          style="font-size: 16px; line-height: 30px; color: #ffffff;"
                          >{datetime.now().today().strftime("%D")}</span
                        >
                      </td>
                    </tr>
                  </tbody>
                </table>
              </header>

              <main>
                <div
                  style="
                    margin: 0;
                    margin-top: 70px;
                    padding: 92px 30px 115px;
                    background: #ffffff;
                    border-radius: 30px;
                    text-align: center;
                  "
                >
                  <div style="width: 100%; max-width: 489px; margin: 0 auto;">
                    <h1
                      style="
                        margin: 0;
                        font-size: 24px;
                        font-weight: 500;
                        color: #1f1f1f;
                      "
                    >
                      User Registration OTP
                    </h1>
                    <p
                      style="
                        margin: 0;
                        margin-top: 17px;
                        font-size: 16px;
                        font-weight: 500;
                      "
                    >
                      Hey {name},
                    </p>
                    <p
                      style="
                        margin: 0;
                        margin-top: 17px;
                        font-weight: 500;
                        letter-spacing: 0.56px;
                      "
                    >
                      Thank you for choosing QuickBite CMS. Use the following OTP
                      to complete the registration. OTP is valid for
                      <span style="font-weight: 600; color: #1f1f1f;">5 minutes</span>.
                      Do not share this code with others, including the QuickBite team.
                      <br>
                      If this wasn't you, then you can safely ignore this email.
                    </p>
                    <p
                      style="
                        margin: 0;
                        margin-top: 60px;
                        font-size: 40px;
                        font-weight: 600;
                        letter-spacing: 25px;
                        color: #ba3d4f;
                      "
                    >
                      {otp}
                    </p>
                  </div>
                </div>

                <p
                  style="
                    max-width: 400px;
                    margin: 0 auto;
                    margin-top: 90px;
                    text-align: center;
                    font-weight: 500;
                    color: #8c8c8c;
                  "
                >
                  Need help? Ask at
                  <a
                    href="mailto:archisketch@gmail.com"
                    style="color: #499fb6; text-decoration: none;"
                    >quickbite.sfit@gmail.com</a
                </p>
              </main>

              <footer
                style="
                  width: 100%;
                  max-width: 490px;
                  margin: 20px auto 0;
                  text-align: center;
                  border-top: 1px solid #e6ebf1;
                "
              >
                <p
                  style="
                    margin: 0;
                    margin-top: 40px;
                    font-size: 16px;
                    font-weight: 600;
                    color: #434343;
                  "
                >
                  QuickBite CMS
                </p>
                <p style="margin: 0; margin-top: 8px; color: #434343;">
                  Mumbai, India 🇮🇳
                </p>
                <div style="margin: 0; margin-top: 16px;">
                  <a href="" target="_blank" style="display: inline-block;">
                    <img
                      width="36px"
                      alt="Facebook"
                      src="https://archisketch-resources.s3.ap-northeast-2.amazonaws.com/vrstyler/1661502815169_682499/email-template-icon-facebook"
                    />
                  </a>
                  <a
                    href=""
                    target="_blank"
                    style="display: inline-block; margin-left: 8px;"
                  >
                    <img
                      width="36px"
                      alt="Instagram"
                      src="https://archisketch-resources.s3.ap-northeast-2.amazonaws.com/vrstyler/1661504218208_684135/email-template-icon-instagram"
                  /></a>
                  <a
                    href=""
                    target="_blank"
                    style="display: inline-block; margin-left: 8px;"
                  >
                    <img
                      width="36px"
                      alt="Twitter"
                      src="https://archisketch-resources.s3.ap-northeast-2.amazonaws.com/vrstyler/1661503043040_372004/email-template-icon-twitter"
                    />
                  </a>
                  <a
                    href=""
                    target="_blank"
                    style="display: inline-block; margin-left: 8px;"
                  >
                    <img
                      width="36px"
                      alt="Youtube"
                      src="https://archisketch-resources.s3.ap-northeast-2.amazonaws.com/vrstyler/1661503195931_210869/email-template-icon-youtube"
                  /></a>
                </div>
                <p style="margin: 0; margin-top: 16px; color: #434343;">
                  Copyright © 2024 QuickBite CMS. All rights reserved.
                </p>
              </footer>
            </div>
          </body>
        </html>
        """

        for user in self.user_data:
            if user['email'] == email:
                user['otp'] = otp
                user['time'] = time.time() + 300
                break

        msg = MessageSchema(
            subject="QuickBite User Registration OTP",
            recipients=[email],
            body=html,
            subtype="html"
        )

        try:
            await fm.send_message(msg)
            return {"message": "Email sent successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def verify_otp(self, otp: str, email: str) -> dict:
        for i, user in enumerate(self.user_data):
            if user['email'] == email:  # Search for the user in user data list
                if user["time"] < time.time():  # If the otp is expired
                    log.info(f"PID: {user['uid']}'s OTP has expired")
                    raise HTTPException(
                        status_code=status.HTTP_406_NOT_ACCEPTABLE,
                        detail="OTP Expired",
                    )
                elif user['otp'] == otp:  # If the otp is correct
                    self.user_data.pop(i)  # Remove the user from the user data
                    user['message'] = False  # Indicates that the otp is correct
                    return user  # Return the user data for that user
                else:  # If password is incorrect
                    log.info("PID %s's OTP is incorrect", user['uid'])
                    raise HTTPException(
                        status_code=status.HTTP_406_NOT_ACCEPTABLE,
                        detail="Incorrect OTP",
                    )
        log.info(f'Email: {email} not requested OTP', user['uid'])
        raise HTTPException(  # If the user is not found in the user data
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
