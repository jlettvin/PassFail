#!/usr/bin/env python

import os
import sys
import string
import getpass
import datetime
import socket
import getpass
import platform
import os.path
import inspect
import locale
import random
import uuid
import pprint

class At(object):
    enabled = True # True for everyone (set False to turn off for everyone)
    indent = 0
    @staticmethod
    def enable(flag = True):
        At.enabled = flag
    def __init__(self, text = '', *arg):
        self.enabled = arg[0] if arg else At.enabled
        self.text = text if text else inspect.stack()[1][3]
        self.indent = ' ' * At.indent
    def __enter__(self):
        if self.enabled:
            print self.indent+'Enter at %s' % (self.text)
        At.indent += int(At.indent < 40)
        return self
    def __exit__(self, type, value, traceback):
        At.indent -= int(At.indent>0)
        if self.enabled:
            print self.indent+'Leave at %s' % (self.text)
    def __call__(self, arg):
        if self.enabled:
            print self.indent+'While at %s: %s' % (self.text, str(arg))

# MAIN ########################################################################
if __name__ == '__main__':
    import unittest

    class AtTest(unittest.TestCase):
        def setUp(self): pass
        def tearDown(self): pass

        def test_001(self):
            print
            with At() as at:
                pass
            with At('visible') as at:
                at('test message')
            with At('visible') as at:
                at('test message')
            with At('invisible', False) as at:
                at('test message')
            At.enable(False)
            with At('visible', False) as at:
                at('test message')
            with At('invisible') as at:
                at('test message')

        def test_002(self):
            print
            At.enable(True)
            with At('layer 1.0') as at:
                with At('layer 1.1', False) as at:
                    with At('layer 1.2', False) as at:
                        with At('layer 1.3', True) as at:
                            pass
            At.enable(False)
            with At('layer 2.0') as at:
                with At('layer 2.1', False) as at:
                    with At('layer 2.2', False) as at:
                        with At('layer 2.3', True) as at:
                            pass

    try: unittest.main()
    except Exception as e: print 'Unexpected error: ', sys.exc_info()[0]
    finally: pass
################################################################################
