"""
Flask extension instances.

Extensions are instantiated here (unbound) and initialized inside the
application factory (app/__init__.py) via `init_app()`. This avoids
circular imports across the project.
"""
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()
