#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
  index = 0
  e = 100
  count = 0
  while True:
    a = (k+index)%len(c) # wraps around the list from the beginning
    if c[a]==1:
      e=e-1-2
    else:
      e=e-1
    count+=1
    index+=k
    if a==0:
      break
  print(f"Energy : {e}, counted wraps:{count} times")
  return e
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
