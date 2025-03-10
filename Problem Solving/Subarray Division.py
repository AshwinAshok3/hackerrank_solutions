#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    # Write your code here
    arr = []
    j = m

    for i in range(0, len(s)):
      # Ensure loop runs correctly
      if j > len(s):  # Prevent index error
            break
        
      arr2 = s[i:j]  # Extract subarray
        
      if sum(arr2) == d:
          arr.append(arr2)

      j += 1  # Increment j to move the window
    
    return len(arr)  # Ensure correct return


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
