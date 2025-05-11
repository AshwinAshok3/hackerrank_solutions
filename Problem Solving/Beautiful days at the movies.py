#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#

def beautifulDays(i, j, k):
    # # Write your code here
    # print(f"Starting Number : {i}")
    # print(f"Ending Number : {j}")
    # print(f"Divisor : {k}")
    
    # print(f"\nAll the numbers in that range [{i}-{j}] are :")
    count = 0
    for num in range(i,j+1):
      a = list(str(num))
      reverse_num = int(("").join(a[::-1] ))
      diff = num - reverse_num
      percen = diff%k
      if percen <= 0 :
        count+=1
      
    return count
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
