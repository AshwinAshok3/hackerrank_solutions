#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n -> page length
#  2. INTEGER p -> target page
#

def pageCount(n, p):
    # Write your code here
    
    # normal array list
    ar = []
    # subarray list
    ar2 = []
    
    if n%2==0:
      ar = [i for i in range(0,n+1)]
      ar.append(0)
    else:
      ar = [i for i in range(0,n+1)]
    print(ar)    

    # making sub arrays
    for i in range(0, len(ar)-1, 2):
      ar2.append([ar[i], ar[i+1]])
    print(ar2)
    
    
    front_count = 0
    back_count = 0
    
    for i in range(0,len(ar2)):
      if p in ar2[i]:
        break
      else:
        front_count+=1
    
    for i in range(len(ar2)-1,-1,-1):
      if p in ar2[i]:
        break
      else:
        back_count+=1
    
    print(f"front count  = {front_count}")
    print(f"back count  = {back_count}")

  
    if front_count>back_count:
      return back_count
    elif back_count>front_count:
      return front_count
    elif back_count==front_count:
      return front_count
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
