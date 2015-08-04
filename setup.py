#!/usr/bin/env python3

import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    """
    From http://pytest.org/latest/goodpractises.html
    """
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

if __name__ == "__main__":
    setup(name='PyPrint',
          description='A library providing printing facilities for python '
                      'applications.',
          author="Lasse Schuirmann",
          author_email='lasse.schuirmann@gmail.com',
          maintainer='Lasse Schuirmann',
          maintainer_email='lasse.schuirmann@gmail.com',
          platforms='any',
          packages=find_packages(exclude=["build.*", ".*tests.*", ".*tests"]),
          install_requires=["setuptools"],
          license="AGPL v3",
          tests_require=['pytest'],
          cmdclass={'test': PyTest})