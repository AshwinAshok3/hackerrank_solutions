#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    ht = 1
    print(f"For the cycle num : {n}")
    for cyc_num in range(0,n):
      print(f"cycle num : {cyc_num} : before cycle : {ht}")
      if ht%2!=0:
        ht*=2
      else:
        ht+=1        
      print(f"cycle num : {cyc_num} : after cycle : {ht}")
    
    return ht

    
      
      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
