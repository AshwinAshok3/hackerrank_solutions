#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    nw_a = []

    for i in a:
        z = []
        for j in range(1,101):   # 101 because, the constraint given in the question is (1<=a[i]<=100)  and  (1<=b[j]<=100)
            if (i*j)>100:
                break
            else:
                z.append(i*j)
        nw_a.append(list(z))
      
    # print(nw_a)
    new_a_set = set(nw_a[0]).intersection(*nw_a[1:])
    # print(new_a_set)

    b1 = []
    for j in new_a_set:
        if all(i % j == 0 for i in b):  # why all(), because i couldn't think of any other alternative to calculate all the elements in the b array with a for loop because whenever i do i fail at the test cases
            b1.append(j)
          
    # print(b1)
    b_set = set(b1)
    return len(b_set)
    
          

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
