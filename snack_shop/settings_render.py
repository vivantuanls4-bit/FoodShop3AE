import os

import dj_database_url
from django.core.exceptions import ImproperlyConfigured

from .settings_railway import *


SECRET_KEY = os.environ.get("SECRET_KEY")
if not SECRET_KEY:
    raise ImproperlyConfigured("Set SECRET_KEY in the Render environment.")

DEBUG = False

render_hostname = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
ALLOWED_HOSTS = [render_hostname] if render_hostname else []
ALLOWED_HOSTS.extend(
    host.strip()
    for host in os.environ.get("ALLOWED_HOSTS", "").split(",")
    if host.strip()
)

CSRF_TRUSTED_ORIGINS = (
    [f"https://{render_hostname}"] if render_hostname else []
)
CSRF_TRUSTED_ORIGINS.extend(
    origin.strip()
    for origin in os.environ.get("CSRF_TRUSTED_ORIGINS", "").split(",")
    if origin.strip()
)

DATABASE_URL = os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    raise ImproperlyConfigured("Set DATABASE_URL to your Render PostgreSQL URL.")

DATABASES = {
    "default": dj_database_url.parse(
        DATABASE_URL,
        conn_max_age=600,
        ssl_require=True,
    )
}

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
