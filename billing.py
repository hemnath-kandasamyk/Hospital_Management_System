"""
Billing blueprint.

Defines HTTP routes for the billing module. Routes should stay thin:
validate input, call the service layer, and return a response.
"""
from flask import Blueprint, jsonify

billing_bp = Blueprint("billing", __name__)


@billing_bp.route("/", methods=["GET"])
def list_billing():
    """Example placeholder route for billing. TODO: implement."""
    return jsonify({"message": "Billing route placeholder"}), 200
