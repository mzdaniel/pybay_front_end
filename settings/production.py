import os
from .base import *

DEBUG = False
SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pybay',
        'USER': 'pybay',
        'PASSWORD': os.environ['DB_PASSWD'],
        'HOST': 'localhost',
        'PORT': '',
    }
}
