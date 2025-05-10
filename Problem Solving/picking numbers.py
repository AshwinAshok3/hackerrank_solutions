#!/bin/python3

import math
import os
import random
import re
import sys

# 13465 , [1], [3,3], [4], [5], [6]
# Complete the 'pickingNumbers' function below.
# 4 6 5 3 3 1 
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    '''
    first iterate through all the elements in the list
    until the iteration satisifies 
    '''    
    freq = {}
    # counts = 1
    # Count frequencies of each number
    for num in a:
        freq[num] = freq.get(num, 0) + 1    
    
    p = 0
    for key, value in freq.items():
      curr_val = freq[key] + freq.get(key+1,0)
      p = max(p,curr_val)  
    
    return p

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
