#!/usr/bin/env python

"""
PassFail.py
"""

__date__       = "20130101"
__author__     = "jlettvin"
__maintainer__ = "jlettvin"
__email__      = "jlettvin@gmail.com"
__copyright__  = "Copyright(c) 2013 Jonathan D. Lettvin, All Rights Reserved"
__license__    = "Trade Secret"
__status__     = "Production"
__version__    = "0.0.1"

from Color import Color

#CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
class PassFail(object):
    T = Color(
            foreground = 'green',
            background = 'black',
            render     = 'bright')('[PASS]')
    F = Color(
            foreground = 'red',
            background = 'white',
            render     = 'bright')('[FAIL]')
    prefix = [F, T]

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    @classmethod
    def call(self, TF, msg = None):
        print PassFail.prefix[int(TF)]+(' ' + str(msg) if msg else '')

PF = PassFail.call

#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
if __name__ == "__main__":

    PF(True)
    PF(False)

    PF(True , 'True' )
    PF(False, 'False')

