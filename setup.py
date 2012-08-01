import os
from setuptools import setup, find_packages

import posts


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-posts',
    version=posts.__version__,
    description='A generic posts app for django',
    long_description=read('README.md'),
)
