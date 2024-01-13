from flask_mail import Mail, Message
import random
import os


class OTP:
    def __init__(self, app):
        self.mail = Mail(app)
        self.otp = ""
        self.sender_mail = os.environ.get("ADMIN_MAIL")

    def send_otp(self, email):
        otp = ""
        for _ in range(6):
            otp += str(random.randint(0, 9))
        self.otp = otp
        msg = Message(f"QuickBite: Email Verification OTP [{otp}]", sender=self.sender_mail, recipients=[email])
        msg.html = f'''<h2>OTP is-</h2>\n<h1>{otp}</h1>\n\n<h4>Thanks and Regards,</h4><h4>QuickBite.</h4>'''
        self.mail.send(msg)
        print(otp)

    def verify_otp(self, otp):
        if otp == self.otp:
            return True
        else:
            return False
