"""
Global Configuration for Application
"""
import os
import logging

# Get database password from environment variable
DB_PASSWORD = os.getenv("DB_PASSWORD")

# If DB_PASSWORD is not set, raise an error
if not DB_PASSWORD:
    raise ValueError("Database password not set. Please set the DB_PASSWORD environment variable.")

# Get configuration from environment
DATABASE_URI = os.getenv(
    "DATABASE_URI",
    f"postgresql://postgres:{DB_PASSWORD}@localhost:5432/postgres"
)

# Configure SQLAlchemy
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret for session management
SECRET_KEY = os.getenv("SECRET_KEY", "sup3r-s3cr3t")
LOGGING_LEVEL = logging.INFO
