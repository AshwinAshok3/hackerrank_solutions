#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    # Write your code here
    final_d = 0
    # julian calendars
    if 1700<=year<1918:
      if year%4==0:
        final_d = 256 - 244
      else:
        final_d = 256 - 243
    
    # gregorian calendar
    elif 1919<=year<=2700:
      if year%400==0 or (year%4==0 and year%100!=0):
        final_d = 256 - 244
      else: 
        final_d = 256 - 243
    
    # from jan 31 to NEXT day(tomorrow was) is feb 14 (diff = 13 days missing in 1918 we ought to add it)
    elif year == 1918:
      return f"{(256-243)+13}.09.{year}"
      
    return f"{final_d}.09.{year}"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
