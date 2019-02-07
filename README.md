{% comment "This comment section will be deleted in the generated project" %}

# [Edge][docs]

[![Build Status](https://travis-ci.org/arocks/edge.svg?branch=master)](https://travis-ci.org/arocks/edge)

**A Fantastic Django project starter.**

## Features

* Ready Bootstrap-themed pages
* User Registration/Sign up
* Better Security with [12-Factor](http://12factor.net/) recommendations
* Logging/Debugging Helpers
* Works on Python 3 and Django 2
* Formatted with [Black](https://github.com/ambv/black)

## Quick start:

1. `$ django-admin.py startproject --template=https://github.com/arocks/edge/archive/master.zip --extension=py,md,html,env my_proj`
2. `$ cd my_proj`
3. `$ pip install -r requirements.txt `
4. `$ cd src`
5. `$ cp my_proj/settings/local.sample.env my_proj/settings/local.env`
6. `$ python manage.py migrate`

More information at: [http://django-edge.readthedocs.org/][docs]
Contribute using: [Edge Dev Tools](https://github.com/arocks/edge-devtools)  ✨ 🍰 ✨

[docs]: http://django-edge.readthedocs.org/


## Recommended Installation (with `pipenv`)
1. `$ pip install --user --upgrade pipenv` ([Install pipenv system-wide or locally](https://docs.pipenv.org/) but outside a virtualenv)
2. `$ mkdir my_proj` (choose a better name than `my_proj` for your project)
3. `$ django-admin.py startproject --template=https://github.com/arocks/edge/archive/master.zip --extension=py,md,html,env my_proj .`

    If you get an SSL error, then download the zip file and mention it after `--template=`, like this: `django-admin.py startproject --template=~/Downloads/master.zip --extension=py,md,html,env my_proj .`
4. `$ pipenv install --dev`
5. `$ pipenv shell`
6. `$ cp src/my_proj/settings/local.sample.env src/my_proj/settings/local.env` (or rename this file)
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
