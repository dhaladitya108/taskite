import dj_database_url
from taskite.settings.django_environ import env

DATABASES = {
    # "default": {
    #     "ENGINE": "django.db.backends.sqlite3",
    #     "NAME": BASE_DIR / "db.sqlite3",
    # },
    "default": dj_database_url.config(default=env("DATABASE_URL"))
}