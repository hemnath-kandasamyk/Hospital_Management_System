"""
Report blueprint.

Defines HTTP routes for the report module. Routes should stay thin:
validate input, call the service layer, and return a response.
"""
from flask import Blueprint, jsonify

report_bp = Blueprint("report", __name__)


@report_bp.route("/", methods=["GET"])
def list_report():
    """Example placeholder route for report. TODO: implement."""
    return jsonify({"message": "Report route placeholder"}), 200
