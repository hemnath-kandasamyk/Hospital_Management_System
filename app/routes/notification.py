"""
Notification blueprint.

Defines HTTP routes for the notification module. Routes should stay thin:
validate input, call the service layer, and return a response.
"""
from flask import Blueprint, jsonify

notification_bp = Blueprint("notification", __name__)


@notification_bp.route("/", methods=["GET"])
def list_notification():
    """Example placeholder route for notification. TODO: implement."""
    return jsonify({"message": "Notification route placeholder"}), 200
