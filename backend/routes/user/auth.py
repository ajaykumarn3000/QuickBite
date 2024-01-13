from flask import Blueprint, request, make_response, jsonify
from datetime import datetime

auth_blueprint = Blueprint('user_auth', __name__, url_prefix="/user/auth")
otp_auth = None


def user_auth_blueprint(otp):
    global otp_auth
    otp_auth = otp
    return auth_blueprint


# User Register
@auth_blueprint.route('/register', methods=['POST'])
def user_register():
    print("Incoming request")
    data = request.json
    for key in data:
        print(f"{key}:", data[key])
    print(datetime.now())
    otp_auth.send_otp(data["email"])
    print(datetime.now())
    return_data = {
        "otp": "OTP Sent"
    }
    res = make_response(jsonify(return_data), 200)
    return res


@auth_blueprint.route('/verify', methods=['POST'])
def verify_email():
    data = request.json
    if otp_auth.verify_otp(str(data["otp"])):
        return_data = {
            "res": "success"
        }
        print("Success")
        res = make_response(jsonify(return_data), 200)
    else:
        return_data = {
            "message": "Incorrect OTP"
        }
        res = make_response(jsonify(return_data), 400)
    return res


# User Login
@auth_blueprint.route('/login')
def user_login():
    return 'This is the authentication route'
