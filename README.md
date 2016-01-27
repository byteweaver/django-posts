django-posts
============

A generic django application to kick start nearly any kind of post handling.

## Key features

* very generic implementation and modular structure
* easy to customize and extend

## Installation

If you want to install the latest stable release from PyPi:

    $ pip install django-posts

If you want to install the latest development version from GitHub:

    $ pip install -e git://github.com/byteweaver/django-posts#egg=django-posts

Add `posts` to your `INSTALLED_APPS`:

    INSTALLED_APPS = (
        ...
        'posts',
        ...
    )

Hook this app into your ``urls.py``:

    urlpatterns = patterns('',
        ...
        url(r'^posts/', include('posts.urls', namespace='posts')),
        ...
    )

## Testing

You require `tox` in order to run the unittests of this project:

    pip install tox

Then just run tox in the project's folder:

    $ tox

## Versions

The last upgrade, as starting with version 0.2.x, is incompatible with all versions below and does no longer feature south support!

- version 0.2.x requires Django 1.5
- all versions below run with Django1.4 (and maybe below, not tested)

### Version 0.3

- update app to work with python3 and django1.8
