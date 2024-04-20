import os
import dj_database_url

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # },
    "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}