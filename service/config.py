"""
Global Configuration for Application
"""
import os
import logging
from urllib.parse import urlparse, urlunparse
from getpass import getpass

# Function to get password securely
def get_db_password():
    return getpass("Enter database password: ")

# Get configuration from environment
DATABASE_URI = os.getenv(
    "DATABASE_URI",
    "postgresql://postgres@localhost:5432/postgres"
)

# Parse the DATABASE_URI
parsed_uri = urlparse(DATABASE_URI)

# Get the password securely
db_password = get_db_password()

# Reconstruct the URI with the password
protected_uri = urlunparse(
    (parsed_uri.scheme, 
     f"{parsed_uri.username}:{db_password}@{parsed_uri.hostname}:{parsed_uri.port}",
     parsed_uri.path, 
     parsed_uri.params, 
     parsed_uri.query, 
     parsed_uri.fragment)
)

# Configure SQLAlchemy
SQLALCHEMY_DATABASE_URI = protected_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret for session management
SECRET_KEY = os.getenv("SECRET_KEY", "sup3r-s3cr3t")
LOGGING_LEVEL = logging.INFO
