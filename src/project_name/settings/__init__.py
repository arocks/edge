# In production set the environment variable like this
# $ export DJANGO_SETTINGS_MODULE=cherry_cakes.settings.production

try:
    from .development import *
except ImportError:
    pass
