import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Use environment variable when available for better security in deployments
    SECRET_KEY = os.environ.get("SECRET_KEY", "change_this_secret_key")
    # Toggle debug via FLASK_DEBUG=1 in the environment
    DEBUG = os.environ.get("FLASK_DEBUG", "0") == "1"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or ("sqlite:///" + os.path.join(BASE_DIR, "app.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Central upload folder (relative to project)
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
    # Max upload size (5 MB)
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024
    # Allowed image extensions for uploads
    ALLOWED_IMAGE_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
