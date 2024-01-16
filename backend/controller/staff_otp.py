from os import environ
import time
from datetime import datetime
from pyotp import TOTP, random_base32
from fastapi import APIRouter, HTTPException
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

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
    """A class which is used to generate an OTP and temporary flow of user data"""

    def __init__(self):
        # This list contains all the active user data (otp, email, etc.)
        self.user_data = []
        self.sender_email = environ.get('ADMIN_MAIL')

    async def send_otp(self, email: str) -> dict:

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
                              Staff Registration OTP
                            </h1>
                            <p
                              style="
                                margin: 0;
                                margin-top: 17px;
                                font-size: 16px;
                                font-weight: 500;
                              "
                            >
                              Hey Administrator,
                            </p>
                            <p
                              style="
                                margin: 0;
                                margin-top: 17px;
                                font-weight: 500;
                                letter-spacing: 0.56px;
                              "
                            >
                              {email} has chosen to register as a staff member. Use the 
                              following OTP to complete the registration. OTP is valid for
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

        # Search the entire user data
        for user in self.user_data:
            # If there is a user who has already requested the otp before
            if user['email'] == email:
                print('user found')
                # Replace the old otp with the new otp
                user['otp'] = otp
                # Give him/her some extra time to verify the new otp
                user['time'] = time.time() + 300
                # Stop searching for the user
                break
        print("Sending OTP")
        print(self.user_data)

        msg = MessageSchema(
            subject="QuickBite Staff Registration OTP",
            recipients=[environ.get('ADMIN_MAIL')],
            body=html,
            subtype="html"
        )

        try:
            await fm.send_message(msg)
            print("OTP sent")
            print(self.user_data)
            return {"message": "Email sent successfully"}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def verify_otp(self, otp: str, email: str):
        # Search the entire list of user data
        for i, user in enumerate(self.user_data):
            # If there exists a user who has requested to register
            if user['email'] == email:
                # If his otp has expired
                if user["time"] < time.time():
                    return {"message": "OTP Expired"}
                # If the user has entered a correct otp
                elif user['otp'] == otp:
                    # Remove the user from user data
                    self.user_data.pop(i)
                    # For the if condition in
                    user['message'] = False
                    return user
                else:
                    return {"message": "Incorrect OTP"}
            return {"message": "User not found"}
