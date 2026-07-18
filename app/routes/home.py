from flask import Blueprint, jsonify

# Create a Blueprint
home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    return "<h1>🏥 Welcome to Hospital Management System</h1>"


@home_bp.route("/about")
def about():
    return "<h2>Hospital Management System Backend API</h2>"


@home_bp.route("/health")
def health():
    return jsonify({
        "status": "running",
        "application": "Hospital Management System",
        "version": "1.0.0"
    })
