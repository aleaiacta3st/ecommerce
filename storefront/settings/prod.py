import os
import dj_database_url
from .common import *

print("=" * 50)
print("LOADING PROD.PY!")
print("=" * 50)

DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY', 'temp-key')
ALLOWED_HOSTS = []


DATABASES = {
    'default': dj_database_url.config()
}
