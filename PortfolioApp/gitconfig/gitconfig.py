import os
from dotenv import load_dotenv

# Load environment variables from .env file for local development
load_dotenv()

# GitHub Configuration
TOKEN = os.getenv('TOKEN', 'default_token')

# Database Configuration
DNAME = os.getenv('DB_NAME', 'default_db_name')
DUSER = os.getenv('DB_USER', 'default_user')
DPASSWORD = os.getenv('DB_PASSWORD', 'default_password')
DHOST = os.getenv('DB_HOST', 'localhost')
DPORT = os.getenv('DB_PORT', '5432')

# Django Secret Key
set = os.getenv("DJANGO_SECRET_KEY", "default_django_secret")

