from .base import *
from decouple import config

DEBUG = True
ALLOWED_HOSTS = ["*"]

# PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT", default="5432"),
        "OPTIONS": {
            "client_encoding": "UTF8",
        },
    }
}

# Django-debug-toolbar
INSTALLED_APPS += [
    "debug_toolbar",
    "apps.blog",
    "corsheaders",
]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]


CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",  # ← React dev-сервер
]

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]

INTERNAL_IPS = ["127.0.0.1", "localhost"]
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: True}

# Email в консоль
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


