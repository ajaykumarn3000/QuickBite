from flask import Blueprint, request, make_response, jsonify
from datetime import datetime

auth_blueprint = Blueprint('user_api', __name__, url_prefix="/user/api")

# TODO: Get all available Products
# GET /menu
# Returns a list of all available products

# TODO: Get the cart details
# GET /cart
# Returns a list of all products in the cart

# TODO: Add a product to cart
# POST /cart/<product_id>
# Removes the product from the cart
# Returns the added product

# TODO: Remove a product from cart
# DELETE /cart/<product_id>
# Removes the product from the cart
# Returns the removed product

# TODO: Payment


