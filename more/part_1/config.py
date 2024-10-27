import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

AUTH_JWT_SECRET = os.getenv('AUTH_JWT_SECRET')
AUTH_JWT_SECRET_2 = os.getenv('AUTH_JWT_SECRET_2')
