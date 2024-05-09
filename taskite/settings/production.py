import os
from taskite.settings.base import *
import dj_database_url
from dotenv import load_dotenv
import sentry_sdk

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN"),
    enable_tracing=True,
)
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

AWS_BUCKET_NAME = os.environ.get("AWS_BUCKET_NAME")
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY")
AWS_REGION = os.environ.get("AWS_REGION")
AWS_ENDPOINT = os.environ.get("AWS_ENDPOINT", None)

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS": {
            "bucket_name": AWS_BUCKET_NAME,
            "access_key": AWS_ACCESS_KEY,
            "secret_key": AWS_SECRET_KEY,
            "region_name": AWS_REGION
        },
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}