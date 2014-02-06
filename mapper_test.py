#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
mapper_test.py

mapper unit tests. post_b2bua-911-mining

@author:  Luis Martin Gil
@contact: martingil.luis@gmail.com
@website: www.luismartingil.com
@github: https://github.com/luismartingil
'''

import unittest
import datetime

from mapper import map

year=2013
year_dec=str(year)[2:]
date_ini=datetime.datetime(year, 1, 1, 0, 0)
date_end=datetime.datetime(year, 12, 31, 23, 59)

# <line> <expected>
tests = \
    [    

    # test
    [
        '23 Jan 13:28:44.351/GLOBAL/b2bua: ruri options parsed',
        {
            'eday' : '01/23/%s' % year_dec,
            'dayow' : '3Wed',
            'hourod' : '13PM',
            }
        ],

    # test
    [
        '23 Jan 13:26:15.365aisudhasiodhas/GLOBAL/b2bua: ruri options parsed',
        {
            'eday' : '01/23/%s' % year_dec,
            'dayow' : '3Wed',
            'hourod' : '13PM',
            }
        ],

    # test
    [
        '23 Jan 13:26:15.365aisudhasiodhas/GLOBAL/b2bua: ruri options parsed 7w8efbw78fq',
        {
            'eday' : '01/23/%s' % year_dec,
            'dayow' : '3Wed',
            'hourod' : '13PM',
            }
        ],


    # test
    [
        '22 Mar 13:26:15.365aisudhasiodhas/GLOBAL/b2bua: ruri options parsed',
        {
            'eday' : '03/22/%s' % year_dec,
            'dayow' : '5Fri',
            'hourod' : '13PM',
            }
        ],

    # test
    [
        '1 Jun 13:26:15.365aisudhasiodhas/GLOBAL/b2buadwdqwd: ruri options parsed 7w8efbw78fq',
        {
            'eday' : '06/01/%s' % year_dec,
            'dayow' : '6Sat',
            'hourod' : '13PM',
            }
        ],

    # test
    [
        '1 Jun 13:26:15.365aisudhasiodhas/GLOBAL/b2buadwdqwd: ruri options parseddd 7w8efbw78fq',
        {
            'eday' : '06/01/%s' % year_dec,
            'dayow' : '6Sat',
            'hourod' : '13PM',
            }
        ],

    
    ]

class Test_Apply(unittest.TestCase):
    pass

def test_Function_mapper(t):
    def test(self):
        input, desired = t[0], t[1]        
        for key,value in desired.iteritems():
            self.assertEqual(map(key, input, output=False,
                                 year=year,
                                 date_ini=date_ini, 
                                 date_end=date_end), value)
    return test

def attach(where, desc, fun, l):
    """ Attaches tests. DRY function helper. """
    for a, b in [("test-%.6i" % (l.index(x)), fun(x)) \
                     for x in l]:
        setattr(where, a, b)

def suite():
    test_suite = unittest.TestSuite()
    attach(Test_Apply, 
           "test_Function_mapper_true", 
           test_Function_mapper, 
           tests)
    test_suite.addTest(unittest.makeSuite(Test_Apply))
    return test_suite


if __name__ == '__main__':

    test = True

    if test:
        mySuit=suite()
        runner=unittest.TextTestRunner(verbosity=2)
        runner.run(mySuit)
        print 'Should be %i tests' % (len(tests))
        print '~' * 60


        # Desired output:
        # test-000000 (__main__.Test_Apply) ... ok
        # test-000001 (__main__.Test_Apply) ... ok
        # test-000002 (__main__.Test_Apply) ... ok
        # test-000003 (__main__.Test_Apply) ... ok
        # test-000004 (__main__.Test_Apply) ... ok
        # test-000005 (__main__.Test_Apply) ... ok
        
        # ----------------------------------------------------------------------
        # Ran 6 tests in 0.002s
        
        # OK
        # Should be 6 tests
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
