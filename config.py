# config.py
import os
from dotenv import load_dotenv

# Load environment variables from the .env file.
load_dotenv()

class Config:
    # Secret key for session management. In production, use a strong random key.
    SECRET_KEY = os.getenv("SECRET_KEY", "your_default_secret_key")
    
    # Database configuration using the DATABASE_URL from the .env file.
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///cloud_db.sqlite3")
    
    # Disable modification tracking for performance.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
