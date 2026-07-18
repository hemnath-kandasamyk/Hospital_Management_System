"""
Patient blueprint.

Defines HTTP routes for the patient module. Routes should stay thin:
validate input, call the service layer, and return a response.
"""
from flask import Blueprint, jsonify

patient_bp = Blueprint("patient", __name__)


@patient_bp.route("/", methods=["GET"])
def list_patient():
    """Example placeholder route for patient. TODO: implement."""
    return jsonify({"message": "Patient route placeholder"}), 200
