#!/usr/bin/env python

"""
__init__.py.py: @TODO short description.

@TODO long description if needed.

"""

import logging

__copyright__ = """
Copyright (C) SayMama Ltd 2012

All rights reserved. Any use, copying, modification, distribution and selling
of this software and it's documentation for any purposes without authors' 
written permission is hereby prohibited.
"""

__author__ = 'Tadeusz Kozak'
__email__ = 'tadeusz@saymama.com'
__date__ = '13.03.12 20:55'

log = logging.getLogger(__name__)

class BaseScaffold(object):
    name = ''
    description = ''

    def __init__(self, options):
        print "Creating base scaffold with kwargs: "
        for k, v in options.items():
            print "{0} -> {1}".format(k, v)
        pass