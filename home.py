"""
Home blueprint.

Defines HTTP routes for the home module. Routes should stay thin:
validate input, call the service layer, and return a response.
"""
from flask import Blueprint, jsonify

home_bp = Blueprint("home", __name__)


@home_bp.route("/", methods=["GET"])
def list_home():
    """Example placeholder route for home. TODO: implement."""
    return jsonify({"message": "Home route placeholder"}), 200
