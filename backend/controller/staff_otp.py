import smtplib
from os import environ
import time
from pyotp import TOTP, random_base32
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi import FastAPI, HTTPException
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
"""
app = FastAPI()

# Mail configuration
mail_config = ConnectionConfig(
    MAIL_USERNAME=environ.get('ADMIN_MAIL'),
    MAIL_PASSWORD=environ.get('PASSWORD'),
    MAIL_FROM=environ.get('ADMIN_MAIL'),
    MAIL_PORT=465,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_SSL_TLS=False,
    MAIL_STARTTLS=False
)

# FastMail instance
fm = FastMail(mail_config)


# Route to send email
@app.get("/email")
async def send_email():
    msg = MessageSchema(
        subject="Hello",
        recipients=["kevin.nadar@pm.me"],
        body="Hello",
        subtype="html"
    )
    try:
        await fm.send_message(msg)
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
"""


class OTP:
    """A class which is used to generate an OTP and temporary flow of user data"""

    def __init__(self):
        # This list contains all the active user data (otp, email, etc.)
        self.user_data = []
        self.sender_email = environ.get('ADMIN_MAIL')

    def send_otp(self, email: str) -> None:

        otp = TOTP(random_base32()).now()

        # Email configuration
        receiver_email = environ.get('ADMIN_MAIL')
        subject = "OTP for QuickBite Staff registration"
        body = f"Your OTP is {otp}.\nExpires in 5 minutes."

        # Set up the MIME structure
        message = MIMEMultipart()
        message.attach(MIMEText(body, "plain"))
        message["From"] = self.sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

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

        # Connect to the SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            # Start TLS for security
            server.starttls()

            # Login to your Gmail account
            server.login(self.sender_email, environ.get('PASSWORD'))

            # Send the email
            server.sendmail(self.sender_email, receiver_email, message.as_string())
        print("OTP sent")

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
