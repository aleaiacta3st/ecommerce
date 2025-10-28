"""
WSGI config for storefront project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application 

# wsgi.py
from django.conf import settings
print("DJANGO_SETTINGS_MODULE =", os.getenv("DJANGO_SETTINGS_MODULE"))
print("ALLOWED_HOSTS =", settings.ALLOWED_HOSTS)
print("CSRF_TRUSTED_ORIGINS =", settings.CSRF_TRUSTED_ORIGINS)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storefront.settings.prod')

application = get_wsgi_application()
