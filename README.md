{% comment "This comment section will be deleted in the generated project" %}

# [Edge (beta)][docs]

[![Build Status](https://travis-ci.org/arocks/edge.svg?branch=django3)](https://travis-ci.org/arocks/edge)

**A Fantastic Django project starter.**

## Features

* Ready Bootstrap-themed pages
* User Registration/Sign up
* Better Security with [12-Factor](http://12factor.net/) recommendations
* Logging/Debugging Helpers
* Works on Python 3 and Django 3
* Formatted with [Black](https://github.com/ambv/black)

More information at: [http://django-edge.readthedocs.org/][docs]
Contribute using: [Edge Dev Tools](https://github.com/arocks/edge-devtools)  ✨ 🍰 ✨

[docs]: http://django-edge.readthedocs.org/

## Quick start (Linux)

Before creating a new project from this template, you need to create a fresh virtual environment and install Django:

1. `$ python -m venv ./myenv`
2. `$ source ./myenv/bin/activate` (use the appropriate activate script based on your OS/shell)
3. `$ python -m pip install -U pip wheel django`

Create your new _edgy_ django project (Replace `edgy` in all commands to the name of your project):

1. `$ django-admin startproject --template=https://github.com/arocks/edge/archive/django3.zip --extension=py,md,html,env edgy`
2. `$ cd edgy`
3. `$ pip install -r requirements.txt `
4. `$ cd src`
5. `$ cp edgy/settings/local.sample.env edgy/settings/local.env`
6. `$ python manage.py migrate`
7. `$ python manage.py createsuperuser`
8. `$ python manage.py runserver`


Rest of this README will be copied to the generated project.

--------------------------------------------------------------------------------------------

{% endcomment %}

# {{ project_name }}

{{ project_name }} is a _short description_. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* App1 (short desc)
* App2 (short desc)
* `users` (Custom User model with user profile views)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv {{ project_name }}`
    2. `$ . {{ project_name }}/bin/activate`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
