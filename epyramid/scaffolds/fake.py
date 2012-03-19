# (c) 2012 Ted Kozak and contributors; 
# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license.php


"""
epcreate.py: @TODO short description.

@TODO long description if needed.

"""

import logging
from epyramid.scaffolds import BaseScaffold

__copyright__ = "MIT license http://www.opensource.org/licenses/mit-license.php"
__author__ = 'Tadeusz Kozak'
__email__ = 't_kozak@about.me'
__date__ = '19.03.12 22:26'

log = logging.getLogger(__name__)

class FakeScaffold(BaseScaffold):
    name = 'fake'
    description = 'Equally Fake description of fake scaffold'