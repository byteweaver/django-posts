import os
from setuptools import setup, find_packages

import posts


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-posts',
    version=posts.__version__,
    description='A generic posts app for django (fork of the django-posts)',
    long_description=read('README.md'),
    license='MIT License',
    author='Gilson Filho',
    author_email='contato@gilsondev.com',
    url='https://github.com/gilsondev/django-posts',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django',
        'South',
    ],
    tests_require=[
        'Django',
        'django-nose',
        'coverage',
        'django-coverage',
    ],
    test_suite='posts.tests.runtests.runtests',
)
