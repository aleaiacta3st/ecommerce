import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "storefront.settings.prod")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# (optional) verify at runtime
if os.getenv("PRINT_DJANGO_SETTINGS") == "1":
    from django.conf import settings
    print("DJANGO_SETTINGS_MODULE =", os.getenv("DJANGO_SETTINGS_MODULE"))
    print("ALLOWED_HOSTS =", settings.ALLOWED_HOSTS)
    print("CSRF_TRUSTED_ORIGINS =", getattr(settings, "CSRF_TRUSTED_ORIGINS", None))

