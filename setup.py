#!/usr/bin/env python

"""
setup.py

Setuptools setup script.

"""

__copyright__ = """
Copyright (C) SayMama Ltd 2012

All rights reserved. Any use, copying, modification, distribution and selling
of this software and it's documentation for any purposes without authors' 
written permission is hereby prohibited.
"""

__author__ = 'Tadeusz Kozak'
__email__ = 'tadeusz@saymama.com'
__date__ = '13.03.12 20:53'

__version__ = '0.0.1'

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
meta = os.path.join(here, 'meta')
try:
    README = open(os.path.join(here, 'README.txt')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
    ENTRY_POINTS = open(os.path.join(meta, 'entry_points.ini')).read()
except Exception:
    README = ''
    CHANGES = ''
    ENTRY_POINTS = ''


install_requires = [
    'setuptools',
    'pyramid>=1.3b',
    ]

tests_require = install_requires + [
    'nose',
    'WebTest',
    'pyamf',
    ]

setup(name='easy_pyramid',
      version=__version__,
      description='Pyramid made easy - set of tools that easy daily work with pyramid framework',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Intended Audience :: Developers",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP",
          "Framework :: Pyramid",
          ],
      keywords='web wsgi pyramid pylons xml-rpc',
      author="Tadeusz Kozak",
      author_email="t_kozak@about.me",
      url="https://github.com/Pylons/pyramid_rpc",
      license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require=tests_require,
      install_requires=install_requires,
      test_suite="epyramid.tests",
      entry_points=ENTRY_POINTS
)
