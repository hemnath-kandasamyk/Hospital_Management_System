"""
Auth blueprint.

Defines HTTP routes for the auth module. Routes should stay thin:
validate input, call the service layer, and return a response.
"""
from flask import Blueprint, jsonify

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/", methods=["GET"])
def list_auth():
    """Example placeholder route for auth. TODO: implement."""
    return jsonify({"message": "Auth route placeholder"}), 200
