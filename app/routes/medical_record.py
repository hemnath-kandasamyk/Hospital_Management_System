"""
Medical Record blueprint.

Defines HTTP routes for the medical_record module. Routes should stay thin:
validate input, call the service layer, and return a response.
"""
from flask import Blueprint, jsonify

medical_record_bp = Blueprint("medical_record", __name__)


@medical_record_bp.route("/", methods=["GET"])
def list_medical_record():
    """Example placeholder route for medical_record. TODO: implement."""
    return jsonify({"message": "Medical Record route placeholder"}), 200
