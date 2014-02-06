#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
reducer.py

Hadoop reducer. post_b2bua-911-mining

@author:  Luis Martin Gil
@contact: martingil.luis@gmail.com
@website: www.luismartingil.com
@github: https://github.com/luismartingil
'''

import sys

counter = {}

def main(separator='\t'):
    # Once we have a proper key to map for lets go a read the input
    while 1:
        try:
            line = sys.stdin.readline()
            data = line.rstrip().split(separator, 1)
            key, val = data
            if counter.has_key(key):
                counter[key] += int(val)
            else:
                counter[key] = int(val)
        except KeyboardInterrupt:
            break
        except Exception, msg:
            pass
        if not line:
            break
    for out_key in sorted(counter.keys()):
        print >>sys.stdout, '%s%s%s' % (out_key, separator, counter[out_key])

if __name__ == "__main__":
    main()
