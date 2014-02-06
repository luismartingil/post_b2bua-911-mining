#! /usr/bin/env python
'''
mapper.py

Hadoop mapper. post_b2bua-911-mining

@author:  Luis Martin Gil
@contact: martingil.luis@gmail.com
@website: www.luismartingil.com
@github: https://github.com/luismartingil
'''

import datetime
import re
import sys
import calendar
import os

# Lets set our desired range
year_default=2013
date_ini_default=datetime.datetime(year_default, 9, 1, 0, 0)
date_end_default=datetime.datetime(year_default, 12, 31, 23, 59)

# Lets define some mappers.
mappers = {    
    'eday' : lambda x:x.strftime("%m/%d/%y"), # eday: 03/22/13 ...
    'dayow' : lambda x:x.strftime("%w%a"), # dayow: Monday, Tuesday, Wednesday ...    
    'hourod' : lambda x:x.strftime("%H%p"), # hourod : 1pm, 2pm, 3pm, 4pm ...
    'minoh' : lambda x:x.strftime("%M"), # minoh : 0, 1, 2, 3, ... 59 ...
    'eweek' : lambda x:x.strftime("%W"), # eweek: 1, 2, 3 ...
    'dayow_hourod' : lambda x:x.strftime("%w%a%H%p"), # dayow_hourod : Mondays00am, Mondays01am ...    
    'hourod_dayow' : lambda x:x.strftime("%H%p%w%a") # hourod_dayow : 00amMonday, 01amMonday ...    
    }

def getMonth(month):
    return [y for x, y in zip(calendar.month_abbr[1:], range(1, 13)) if x == month][0]

def map(key, input, year=year_default, output=True, separator='\t',
        date_ini=date_ini_default, date_end=date_end_default): 
    ret = None
    regex_date = '(?P<day>\d+) (?P<month>\w+) (?P<hour>\d+):(?P<m>\d+):(?P<sec>\d+)'
    regex_rest = '(.*ruri options parsed.*)'
    regex = regex_date + regex_rest
    try:
        # Searching from the start of the string using match.
        day, month, hour, mi, sec =  re.match(regex, input).groups()[0:5]
        # Lets make a valid datetime object so we can play with it
        d = datetime.datetime(year, int(getMonth(month)), int(day), int(hour), int(mi), int(sec), 0)
        if date_ini <= d <= date_end:
            ret = mappers[key](d)
            if output:
                print >>sys.stdout, '%s%s%s' % (ret, separator, 1)
    except Exception, msg:
        pass # Not a problem.
    return ret

if __name__ == "__main__":
    key = None
    try:
        # They is passed as argv[1] or as a env variable env_param_key
        key = sys.argv[1] if (len(sys.argv) > 1) else str(os.environ["PARAM_OPT"])
        if key not in mappers.keys():
            raise Exception('Unknown key:%s' % key)
    except Exception, msg:
        sys.exit(str(msg) + '\nUsage: %s %s' % (sys.argv[0], mappers.keys()))
    else:
        # Once we have a proper key to map for lets go a read the input
        while 1:
            try:
                line = sys.stdin.readline()
            except KeyboardInterrupt:
                break
            if not line:
                break
            # Execute the mapping function
            map(key, line)
