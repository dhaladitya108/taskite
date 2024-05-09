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

AWS_BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME")
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
AWS_REGION = os.environ.get("AWS_REGION", None)
AWS_ENDPOINT = os.environ.get("AWS_ENDPOINT")

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": AWS_BUCKET_NAME,
            "access_key": AWS_ACCESS_KEY,
            "secret_key": AWS_SECRET_KEY,
            "endpoint_url": AWS_ENDPOINT,
        },
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}