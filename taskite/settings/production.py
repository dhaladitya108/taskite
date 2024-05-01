import os
from taskite.settings.base import *
import dj_database_url
from dotenv import load_dotenv

# Enable this if you want to pic environment variables from .env file in a prod env.
# load_dotenv()

DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")

DJANGO_VITE_DEV_MODE = False
DJANGO_VITE_MANIFEST_PATH = BASE_DIR / "static/dist/manifest.json"
DJANGO_VITE_STATIC_URL_PREFIX = "dist"

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS").split(",")
CORS_URLS_REGEX = r"^/api/.*$"

DATABASES = {
    "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}