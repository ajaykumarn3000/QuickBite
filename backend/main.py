from flask import Flask
from flask_cors import CORS
import os
# Routes
from routes.user.auth import user_auth_blueprint
# Controller
from controller.otp import OTP

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quickbite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"

CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = EMAIL_ID = os.environ.get("ADMIN_MAIL")
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

otp_auth = OTP(app)

app.register_blueprint(user_auth_blueprint(otp_auth))


if __name__ == "__main__":
    app.run(debug=True)
