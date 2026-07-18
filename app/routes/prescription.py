"""
Prescription blueprint.

Defines HTTP routes for the prescription module. Routes should stay thin:
validate input, call the service layer, and return a response.
"""
from flask import Blueprint, jsonify

prescription_bp = Blueprint("prescription", __name__)


@prescription_bp.route("/", methods=["GET"])
def list_prescription():
    """Example placeholder route for prescription. TODO: implement."""
    return jsonify({"message": "Prescription route placeholder"}), 200
