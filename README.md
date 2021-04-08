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

## Quick start:

Before creating a new project from this template, you need to create a fresh virtual environment and install Django:

1. `$ python -m venv ./myenv`
2. `$ source ./myenv/bin/activate.fish` (use the appropriate activate script based on your shell)
3. `$ python -m pip install -U pip django`

Create your new _edgy_ django project (Replace `edgy` in all commands to the name of your project):

1. `$ django-admin.py startproject --template=https://github.com/arocks/edge/archive/django3.zip --extension=py,md,html,env edgy`
2. `$ cd edgy`
3. `$ pip install -r requirements.txt `
4. `$ cd src`
5. `$ cp edgy/settings/local.sample.env edgy/settings/local.env`
6. `$ python manage.py migrate`
7. `$ python manage.py createsuperuser`
8. `$ python manage.py runserver`


## Recommended Installation (with `pipenv`)
1. `$ pip install --user --upgrade pipenv` ([Install pipenv system-wide or locally](https://docs.pipenv.org/) but outside a virtualenv)
2. `$ mkdir edgy` (choose a better name than `edgy` for your project)
3. `$ django-admin.py startproject --template=https://github.com/arocks/edge/archive/django3.zip --extension=py,md,html,env edgy .`

    If you get an SSL error, then download the zip file and mention it after `--template=`, like this: `django-admin.py startproject --template=~/Downloads/master.zip --extension=py,md,html,env edgy .`
4. `$ pipenv install --dev`
5. `$ pipenv shell`
6. `$ cp src/edgy/settings/local.sample.env src/edgy/settings/local.env` (or rename this file)
7. `$ cd src`
8. `$ python manage.py migrate`
9. `$ python manage.py createsuperuser`
10. `$ python manage.py runserver`

If you need to keep `requirements.txt` updated then run

    pipenv lock --requirements > requirements/base.txt
    echo "-r base.txt" > requirements/development.txt
    pipenv lock --requirements --dev >> requirements/development.txt

Rest of this README will be copied to the generated project.

--------------------------------------------------------------------------------------------

{% endcomment %}

# {{ project_name }}

{{ project_name }} is a _short description_. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* App1 (short desc)
* App2 (short desc)
* App3 (short desc)

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
