"""
Dashboard blueprint.

Defines HTTP routes for the dashboard module. Routes should stay thin:
validate input, call the service layer, and return a response.
"""
from flask import Blueprint, jsonify

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/", methods=["GET"])
def list_dashboard():
    """Example placeholder route for dashboard. TODO: implement."""
    return jsonify({"message": "Dashboard route placeholder"}), 200
