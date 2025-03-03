#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hrs, mn, thrd = s.split(':')
    mn = int(mn)
    ampm = thrd[-2:]
    sec = int(thrd[:2])
    hrs = int(hrs)  
    if ampm == "AM" and hrs == 12:
        hrs = 0 
    elif ampm == "PM" and hrs != 12:
        hrs += 12  
    return f"{hrs:02}:{mn:02}:{sec:02}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
