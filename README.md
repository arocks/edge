> __Delete this blockquote.__
>
> __edge__ - a lighter, cutting-edge Django project skeleton.
>
> FEATURES: Python 3/Django 1.7 support, Bootstrap bundled, No South
>
> Quick start:
> `$ django-admin.py startproject --template=https://github.com/arocks/edge/archive/master.zip --extension=py,md,html,env myproj`
>
> More information at: https://github.com/arocks/edge/wiki

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

    $ python3.4 -m venv {{ project_name }}
    $ . {{ project_name }}/bin/activate

> Sometimes, binaries like pip get installed inside `local/bin/`. So append
> this line to `{{ project_name }}/bin/activate`:
>
> `PATH="$VIRTUAL_ENV/local/bin:$PATH"`

Now the pip commands should work smoothly. Install all dependencies:

    pip install -r dev-requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for a detailed instructions guide.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/


## Setup Using Vagrant
* You will need to have [vagrant](https://www.vagrantup.com/), [virtualbox](https://www.virtualbox.org/) and [ansible](www.ansible.com/) installed. 
* change into this projects directory and:        
`vagrant up`         
* point your browser to; [localhost:8050](http://localhost:8050/)

## python 2.X compatibility
[This fork](https://github.com/komuW/edge) works with python 2.7
