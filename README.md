{% comment "This blockquote will be deleted" %}
 
#edge - a lighter, cutting-edge Django project skeleton.

FEATURES: Python 2.7 or 3.4 / Django 1.7 support, Bootstrap themed, User Registration/Sign up, User 
Profiles

## Quick start:

1. `$ django-admin.py startproject --template=https://github.com/arocks/edge/archive/master.zip --extension=py,md,html,env my_proj`
2. `$ cd my_proj`
3. `$ pip install -r requirements.txt `
4. `$ cd src`
5. `$ python manage.py migrate`

More information at: https://github.com/arocks/edge/wiki


Rest of this README will be copied to the generated project.

--------------------------------------------------------------------------------------------

{% endcomment %}

# {{ project_name }}

{{ project_name }} is a (short description) built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* App1 (short desc)
* App2 (short desc)
* App3 (short desc)

## Installation

### Quick start

To set up a development environment quickly, first install Python 3.4. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3.4 -m venv {{ project_name }}`
    2. `$ . {{ project_name }}/bin/activate`

> Sometimes, binaries like pip get installed inside `local/bin/`. So append
> this line to `{{ project_name }}/bin/activate`:
>
> `PATH="$VIRTUAL_ENV/local/bin:$PATH"`

Now the pip commands should work smoothly. Install all dependencies:

    pip install -r dev-requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the [docs][2] for a detailed instructions guide.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: http://django-edge.readthedocs.org/
