#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):
    # Write your code here
    sort_p = sorted(p).copy() 
    print(f"P : {p}")
    print(f"sorted P : {sort_p}")

    # first index
    index_1_p = []  
    for i in sort_p:
      count=1
      for j in p:
        if i == j:
          index_1_p.append(count)
        count+=1
    print(f"1st Index : {index_1_p}")
  
    # second index
    index2 = []
    for i in index_1_p:
      count1 = 1
      for j in p:
        if j==i:
          print(f"j:{j}, i:{i}, count :{count1}")
          index2.append(count1)
        count1+=1
      
    return index2
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
