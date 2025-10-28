import os
import dj_database_url
from .common import *

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY', 'temporary-key-for-debug')

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://web-production-842d5.up.railway.app']

DATABASES = {
    'default': dj_database_url.config()
}
