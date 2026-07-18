"""
Appointment blueprint.

Defines HTTP routes for the appointment module. Routes should stay thin:
validate input, call the service layer, and return a response.
"""
from flask import Blueprint, jsonify

appointment_bp = Blueprint("appointment", __name__)


@appointment_bp.route("/", methods=["GET"])
def list_appointment():
    """Example placeholder route for appointment. TODO: implement."""
    return jsonify({"message": "Appointment route placeholder"}), 200
