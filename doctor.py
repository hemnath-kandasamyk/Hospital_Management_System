"""
Doctor blueprint.

Defines HTTP routes for the doctor module. Routes should stay thin:
validate input, call the service layer, and return a response.
"""
from flask import Blueprint, jsonify

doctor_bp = Blueprint("doctor", __name__)


@doctor_bp.route("/", methods=["GET"])
def list_doctor():
    """Example placeholder route for doctor. TODO: implement."""
    return jsonify({"message": "Doctor route placeholder"}), 200
