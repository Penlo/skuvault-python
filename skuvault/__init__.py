# -*- coding: utf-8 -*-

'''
Authored by: Nathan Head
'''

import platform
import logging

__version__ = '1.1.2'
Version = __version__  # for backward compatibility

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):

        def emit(self, record):
            pass


log = logging.getLogger('skuvault')

if not log.handlers:
    log.addHandler(NullHandler())


def get_version():
    return __version__
