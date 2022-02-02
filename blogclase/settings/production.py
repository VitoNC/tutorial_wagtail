from .base import *

DEBUG = False

# Arreglar luego


ALLOWED_HOSTS = ['*'] 


try:
    from .local import *
except ImportError:
    pass
