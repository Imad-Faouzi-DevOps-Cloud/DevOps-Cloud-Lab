import os
from flask import Flask
from .routes import user_bp  # Import the Blueprint with routes
from .models import db       # Import SQLAlchemy instance

def create_app():
    """
    Factory function to create and configure the Flask app.
    This function allows creating multiple instances of the app with different configs.
    """
    app = Flask(__name__)

    # Set environment config, fallback to 'production' if not set
    app.config['ENV'] = os.getenv('FLASK_ENV', 'production')

    # Secret key for sessions, CSRF protection, etc.
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-secret')

    # Disable modification tracking to save resources
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Database URI should be set in environment variable or docker-compose (e.g. DATABASE_URL)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///test.db')

    # Initialize SQLAlchemy with this app instance
    db.init_app(app)

    # Register user routes blueprint so /users endpoints work
    app.register_blueprint(user_bp)

    return app

