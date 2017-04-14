from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@yk=67ph&l8t%(4zhfjd8cla2@c)*26n)5#8ebn_m33*b4zi67'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'cfp.db'),
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]
