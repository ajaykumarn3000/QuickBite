from flask import Flask, request, jsonify, make_response, redirect
from flask_cors import CORS, cross_origin
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequestKeyError
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_sqlalchemy import SQLAlchemy
import datetime as dt
from datetime import datetime
import random
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quickbite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "random string"

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = EMAIL_ID = os.environ.get("ADMIN_MAIL")
app.config['MAIL_PASSWORD'] = os.environ.get('PASSWORD')
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

otp = ""


def send_otp(email):
    global otp
    otp = ""
    for _ in range(6):
        otp += str(random.randint(0, 9))

    msg = Message(f"QuickBite: Email Verification OTP [{otp}]", sender=EMAIL_ID, recipients=[email])
    msg.html = f'''<h2>OTP for you Email Verification is-</h2>\n<h1>{otp}</h1>\n\n<h4>Thanks and Regards,</h4><h4>QuickBite.</h4>'''
    mail.send(msg)


@app.route('/auth/register', methods=['POST'])
@cross_origin()
def register():
    global otp
    data = request.json
    for key in data:
        print(f"{key}:", data[key])
    print(datetime.now())
    send_otp(data["email"])
    print(datetime.now())
    return_data = {
        "otp": otp
    }
    print(otp)
    res = make_response(jsonify(return_data), 200)
    return res


@app.route('/auth/verify', methods=['POST'])
@cross_origin()
def verify_email():
    global otp
    data = request.json
    if str(data["otp"]) == otp:
        return_data = {
            "otp": otp
        }
        print("Success")
        res = make_response(jsonify(return_data), 200)
    else:
        return_data = {
            "message": "Incorrect OTP"
        }
        res = make_response(jsonify(return_data), 400)
    return res



#     if User.query.filter_by(email=email).first():
#         # User already exists
#         print("You've already signed up with that email, log in instead!")
#         return redirect(url_for('login'))
#
#     hash_and_salted_password = generate_password_hash(
#         password_form.password.data,
#         method='pbkdf2:sha256',
#         salt_length=8
#     )
#     new_user = User(name=username, email=email, password=hash_and_salted_password, cart={},
#                     address={"name": "", "phone": "", "pincode": "", "locality": "", "address": "", "city": "",
#                              "state": "", "landmark": "", "alt-phone": ""})
#     db.session.add(new_user)
#     db.session.commit()
#     login_user(new_user)


@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    data = request.json
    for key in data:
        print(f"{key}:", data[key])
    return_data = {
        "pid": data["pid"]
    }
    return make_response(jsonify(return_data), 200)


#     login_form = LoginForm()
#     if login_form.validate_on_submit():
#         email = login_form.email.data
#         password = login_form.password.data
#
#         user = User.query.filter_by(email=email).first()
#         # Email doesn't exist or password incorrect.
#         if not user:
#             flash("That email does not exist, please try again.")
#             return redirect(url_for('login'))
#         elif not check_password_hash(user.password, password):
#             flash('Password incorrect, please try again.')
#             return redirect(url_for('login'))
#         else:
#             login_user(user)
#             return redirect(url_for('home'))
#     return render_template("login.html", login_form=login_form)


if __name__ == "__main__":
    app.run(debug=True)
