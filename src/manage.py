#!/usr/bin/env python
from os.path import dirname, join, exists
import os
import sys

import environ

env = environ.Env()
env_file = join(dirname(__file__), '{{ project_name }}/settings/' 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

if __name__ == "__main__":
    # CHANGED manage.py will use development settings by
    # default. Change the DJANGO_SETTINGS_MODULE environment variable
    # for using the environment specific settings file.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.development")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
