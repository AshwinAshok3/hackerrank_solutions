#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    high_score =  int(scores[0])
    low_score = int(scores[0])
    maxi = 0
    mini = 0
    
    for i in range(len(scores)):
      if scores[i] > high_score :
        high_score=scores[i]
        maxi+=1
      elif scores[i] < low_score:
        low_score = scores[i]
        mini+=1
      else:
        high_score = high_score
        low_score = low_score
        maxi = maxi
        mini = mini
    
    return maxi , mini 
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
