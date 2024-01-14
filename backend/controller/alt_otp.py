import smtplib
from os import environ
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
        self.otp = None
        self.uid = None
        self.email = None
        self.passcode = None
        self.sender_email = environ.get('ADMIN_MAIL')

    def send_otp(self, email: str) -> None:

        self.otp = TOTP(random_base32()).now()

        # Email configuration
        receiver_email = self.email = email
        subject = "OTP for QuickBite Service"
        body = f"Your OTP is {self.otp}.\nExpires in 30 seconds."

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
            
    def verify_otp(self, otp: str) -> bool:
        return otp == self.otp
