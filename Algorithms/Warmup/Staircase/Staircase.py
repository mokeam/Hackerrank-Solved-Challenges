#!/bin/python

import sys


n = int(raw_input().strip())
a = n - 1

for i in range(n):
    no_of_space = " "*a
    no_of_chars = "#"*(i+1)
    print "%s%s" % (no_of_space, no_of_chars)
    a = a - 1
