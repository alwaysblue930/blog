from .base import *

SECRET_KEY = env('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

import dj_database_url

DATABASES = {
    'default': dj_database_url.parse(env('DATABASE_URL'))
}
