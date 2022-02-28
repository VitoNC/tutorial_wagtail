from .base import *

DEBUG = False

# Arreglar luego


ALLOWED_HOSTS = ['*','192.168.1.78'] 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mibasededatos',
        'USER': 'victor',
        'PASSWORD': 'calimocho',
        'HOST': 'localhost','192.168.1.78'
        'PORT': '',
    }
}


try:
    from .local import *
except ImportError:
    pass
