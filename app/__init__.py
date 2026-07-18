from flask import Flask


def create_app():
    """
    Application Factory Function

    Creates and configures the Flask application.
    """

    app = Flask(__name__)

    @app.route("/")
    def home():
        return "<h1>🏥 Welcome to Hospital Management System</h1>"

    return app
