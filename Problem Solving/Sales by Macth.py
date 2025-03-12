#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here

    set_ls = list(set(ar))
    pairs = [0*n for i in range(len(set_ls))]
    # print(set_ls)
    
    # counting number of pairs  in the array 
    for i in range(len(set_ls)):
      count = 0
      for j in ar:
        if set_ls[i]==j:
          count+=1      
      pairs[i] = count
    # print(pairs)
       
    # filtering the pairs count
    counts = []
    for i in pairs:
      if i%2==0:
        counts.append(int(i/2))
      elif i%2!=0 and i>1:
        counts.append(int((i-1)/2))
      else:
        counts.append(0)
  
    # print(counts)
    return sum(counts)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
