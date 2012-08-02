import os
import sys

from django.conf import settings

from django_coverage.coverage_runner import CoverageRunner
from django_nose import NoseTestSuiteRunner


EXTERNAL_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
]
INTERNAL_APPS = [
    'django_nose',
    'posts',
]

if not settings.configured:
    settings.configure(
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
        INSTALLED_APPS = EXTERNAL_APPS + INTERNAL_APPS,
        TEMPLATE_DIRS = (
            os.path.join(os.path.dirname(__file__), '../templates'),
        ),
        COVERAGE_MODULE_EXCLUDES = EXTERNAL_APPS,
        COVERAGE_REPORT_HTML_OUTPUT_DIR=os.path.join(os.path.dirname(__file__), 'coverage')
    )


class NoseCoverageTestRunner(CoverageRunner, NoseTestSuiteRunner):
    pass

def runtests(*test_args):
    failures = NoseCoverageTestRunner(verbosity=2, interactive=True).run_tests(test_args)
    sys.exit(failures)

if __name__ == '__main__':
    runtests(*sys.argv[1:])

