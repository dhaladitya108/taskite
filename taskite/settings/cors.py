from taskite.settings.django_environ import env

CORS_ALLOW_ALL_ORIGINS = env("DEBUG")
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])