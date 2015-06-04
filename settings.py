import os

BASE_DIR = os.path.dirname(__file__)

SECRET_KEY = 'xxx'

MIDDLEWARE_CLASSES = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = (
    'myapp',
)
