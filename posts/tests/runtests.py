import sys

from django.conf import settings

from django_coverage.coverage_runner import CoverageRunner
from django_nose import NoseTestSuiteRunner


if not settings.configured:
    settings.configure(
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            }
        },
    )



class NoseCoverageTestRunner(CoverageRunner, NoseTestSuiteRunner):
    pass


def runtests(*test_args):
    failures = NoseCoverageTestRunner(verbosity=2, interactive=True).run_tests(test_args)
    sys.exit(failures)


if __name__ == '__main__':
    runtests(*sys.argv[1:])

