import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings:
    NASA_API_KEY = os.getenv("NASA_API_KEY")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = int(os.getenv("DB_PORT", 5432))
    DB_NAME = os.getenv("DB_NAME")

settings = Settings()