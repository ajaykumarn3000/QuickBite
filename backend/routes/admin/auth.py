from flask import Blueprint, request, make_response, jsonify
from datetime import datetime

auth_blueprint = Blueprint('admin_auth', __name__, url_prefix="/admin/auth")

# TODO: Admin Register
# TODO: Admin Login
