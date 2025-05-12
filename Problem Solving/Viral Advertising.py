#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    # Write your code here
    
    print(n)
    num_of_like = 0
     
    shares = 5
    likes = 2
     
    for i in range(n):
      likes = math.floor(shares/2)
      num_of_like+=likes
      # print(f"Day : {i}, Shared : {shares}, Liked : { likes }, Cummulatives : {num_of_like}")
      shares = likes * 3
    
    return num_of_like

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
