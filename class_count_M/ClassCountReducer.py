#!/usr/bin/python
import re
import sys

(last_key, sum_val) = (None, 0)
for line in sys.stdin:
    (key, val) = line.strip().split("\t")
    if last_key and last_key != key:
        print last_key, "\t", sum_val
        (last_key, sum_val) = (key, int(val))
    else:
        (last_key, sum_val) = (key, sum_val + int(val))

if last_key:
    print last_key, "\t", sum_val
