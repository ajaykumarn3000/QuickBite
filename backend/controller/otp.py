import smtplib
from os import environ
import time
from pyotp import TOTP, random_base32
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fastapi import FastAPI, HTTPException, status
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
        self.user_data = []
        self.sender_email = environ.get('ADMIN_MAIL')

    def send_otp(self, email: str) -> None:

        otp = TOTP(random_base32()).now()

        # Email configuration
        receiver_email = email
        subject = "OTP for QuickBite Service"
        body = f"Your OTP is {otp}.\nExpires in 5 minutes."

        # Set up the MIME structure
        message = MIMEMultipart()
        message.attach(MIMEText(body, "plain"))
        message["From"] = self.sender_email
        message["To"] = receiver_email
        message["Subject"] = subject

        # Connect to the SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            # Start TLS for security
            server.starttls()

            # Login to your Gmail account
            server.login(self.sender_email, environ.get('PASSWORD'))

            # Send the email
            server.sendmail(self.sender_email, receiver_email, message.as_string())

            for user in self.user_data:
                if user['email'] == email:
                    user['otp'] = otp
                    user['time'] = time.time() + 300
                    break
            print("OTP Sent")
            print(self.user_data)

    def verify_otp(self, otp: str, email: str):
        for i, user in enumerate(self.user_data):
            if user['email'] == email:
                if user["time"] < time.time():
                    raise HTTPException(
                        status_code=status.HTTP_406_NOT_ACCEPTABLE,
                        detail="OTP Expired",
                    )
                    # return {"message": "OTP Expired"}
                elif user['otp'] == otp:
                    self.user_data.pop(i)
                    user['message'] = False
                    return user
                else:
                    raise HTTPException(
                        status_code=status.HTTP_406_NOT_ACCEPTABLE,
                        detail="Incorrect OTP",
                    )
                    # return {"message": "Incorrect OTP"}

            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )
            # return {"message": "User not found"}
