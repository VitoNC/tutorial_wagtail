from .base import *

DEBUG = False

# Arreglar luego
SECRET_KEY = 'django-insecure-ljokrzvvwsydc&2d+_d6wd+t#eo2+t*ie3!cnt4ksdw!me9*%i'

ALLOWED_HOSTS = ['*'] 


try:
    from .local import *
except ImportError:
    pass
