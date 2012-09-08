django-posts
============

A generic django application to kick start nearly any kind of post handling.

## Key features

* very generic implementation and modular structure
* easy to customize and extend
* django-south support

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
        url(r'^your-url/$', include('posts.urls')),
        ...
    )