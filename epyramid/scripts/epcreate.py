# (c) 2012 Ted Kozak and contributors; 
# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license.php


"""
epcreate.py: @TODO short description.

@TODO long description if needed.

"""

import logging

SCAFFOLD_GRP_NAME = 'epyramid.scaffold'

__copyright__ = "MIT license http://www.opensource.org/licenses/mit-license.php"
__author__ = 'Tadeusz Kozak'
__email__ = 't_kozak@about.me'
__date__ = '19.03.12 20:53'
__version__ = '0.0.1'

log = logging.getLogger(__name__)

import argparse
import os
import os.path
import pkg_resources
import re
import sys

_bad_chars_re = re.compile('[^a-zA-Z0-9_]')

_OPTIONS = [
    ('-s', '--scaffold', 'scaffold_name', 'append',
     "Blah blah"),
    ('-l', '--list', 'list', 'store_true',
     "List all available scaffold templates"),

]

_DESCRIPTION = """Render Pyramid scaffolding to an output directory"""

def main(argv=sys.argv, quiet=False):
    command = EPCreateCommand(argv, quiet)
    return command.run()


class EPCreateCommand(object):
    """
    Easy Pyramid Create Command - manages project scaffold templates.

    Allows one to create project scaffold using one of predefined template.
    """

    def __init__(self, argv, quiet=False):
        self.quiet = quiet
        self.args = self._input_parser().parse_args(argv[1:])


    def run(self):

        if self.args.action == 'list':
            self.list_scaffolds()
            return 0
        elif self.args.action == 'help':
            pass
        elif self.args.action == 'generate':
            return self.render_scaffold()


    def render_scaffold(self):
        """
        Renders scaffold specified
        """
        scaffold = self.args.scaffold
        self._d("Trying to render scaffold with name {0}".format(scaffold))
        ep = self._get_ep_by_name(scaffold)
        try:
            scaffold_class = ep.load()
            params = {}
            for param in self.args.scaffold_params:
                split = param.split('=')
                if len(split) == 2:
                    params[split[0]] = split[1]
                else:
                    params[split[0]] = True
            scaffold = scaffold_class(params)
        except Exception as e:
            self._e("Failed to load given entry point")
        pass

    def list_scaffolds(self):
        """
        Lists all registered scaffolds in human-readable form to stdout.
        """
        all = self._all_scaffolds()
        print "Currently there are {0} scaffolds registered: ".format(len(all))
        for scaffold in all:
            print "{0}: {1}".format(scaffold.name, scaffold.description)

    def _all_scaffolds(self):
        scaffolds = []
        eps = list(pkg_resources.iter_entry_points(SCAFFOLD_GRP_NAME))
        for entry in eps:
            try:
                scaffolds.append(entry.load())
            except Exception as e: # pragma: no cover
                self._w('Warning: could not load entry point %s (%s: %s)' % (
                    entry.name, e.__class__.__name__, e))
        return scaffolds

    def _get_ep_by_name(self, name):
        eps = list(pkg_resources.iter_entry_points(SCAFFOLD_GRP_NAME))
        for ep in eps:
            if ep.name == name:
                return ep


    def _input_parser(self):
        parser = argparse.ArgumentParser(description=_DESCRIPTION,
                                         version=__version__, )
        parser.add_argument('action',choices=['list','generate', 'help'],
                            help='Action to be performed',nargs='?')
        parser.add_argument(
            'scaffold',action="store",nargs='?',
                            help="Scaffold upon which the action should be performed")
        parser.add_argument('scaffold_params',nargs=argparse.REMAINDER)
        return parser


#    TODO filter them off according to verbosity
    def _d(self, msg):
        print msg

    def _e(self, msg):
        print msg

    def _w(self, msg):
        print msg


