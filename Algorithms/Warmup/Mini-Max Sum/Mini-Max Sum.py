#!/bin/python

import sys

arr = map(int, raw_input().strip().split(' '))
total = [0 for x in range(5)]

for i in range(0, 5):
    if i == 0:
        continue
    total[0] += arr[i]

for i in range(0, 5):
    if i == 1:
        continue
    total[1] += arr[i]

for i in range(0, 5):
    if i == 2:
        continue
    total[2] += arr[i]

for i in range(0, 5):
    if i == 3:
        continue
    total[3] += arr[i]

for i in range(0, 5):
    if i == 4:
        continue
    total[4] += arr[i]

print min(total), max(total)
