from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

import dj_database_url

DATABASES = {
    'default': dj_database_url.parse(env('DATABASE_URL'))
}
