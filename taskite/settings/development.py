import os
import dj_database_url
from dotenv import load_dotenv

from taskite.settings.base import *

load_dotenv()

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", default="127.0.0.1,localhost").split(",")

DJANGO_VITE_DEV_MODE = True
# DJANGO_VITE_MANIFEST_PATH = BASE_DIR / "static/dist/manifest.json"
# DJANGO_VITE_STATIC_URL_PREFIX = "dist"

CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS", default="http://127.0.0.1,http://localhost").split(",")
CORS_URLS_REGEX = r"^/api/.*$"

DATABASES = {
    "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}