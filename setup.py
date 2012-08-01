import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-posts',
    description='A generic posts app for django',
    long_description=read('README.md'),
)
