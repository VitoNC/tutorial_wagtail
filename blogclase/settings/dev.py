from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ljokrzvvwsydc&2d+_d6wd+t#eo2+t*ie3!cnt4ksdw!me9*%i'

# SECURITY WARNING: define the correct hosts in production!
<<<<<<< HEAD
ALLOWED_HOSTS = ['*','192.168.1.78'] 
=======
ALLOWED_HOSTS = ['*','10.6.9.156'] 
>>>>>>> trabajo

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
