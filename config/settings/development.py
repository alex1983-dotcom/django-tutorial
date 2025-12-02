# config/settings/development.py
from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

# SQLite для простоты
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Django-debug-toolbar
INSTALLED_APPS += [
    "debug_toolbar",
    "apps.blog",
]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = ["127.0.0.1", "localhost"]
DEBUG_TOOLBAR_CONFIG = {"SHOW_TOOLBAR_CALLBACK": lambda request: True}

# Email в консоль
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

