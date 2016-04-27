"""
WSGI config for {{ project_name }} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""
from os.path import dirname, join, exists
import os

from django.conf import settings
from django.core.wsgi import get_wsgi_application
import environ
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.production")
application = get_wsgi_application()

env = environ.Env()
env_file = join(dirname(__file__), 'settings/' 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

# Wrap werkzeug debugger if DEBUG is on
if settings.DEBUG:
    try:
        import django.views.debug
        import six
        from werkzeug.debug import DebuggedApplication

        def null_technical_500_response(request, exc_type, exc_value, tb):
            six.reraise(exc_type, exc_value, tb)

        django.views.debug.technical_500_response = null_technical_500_response
        application = DebuggedApplication(application, evalex=True)
    except ImportError:
        pass
