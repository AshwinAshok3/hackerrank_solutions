#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2

'''
we have to formulate a formula on our own to solve this problem 
it was nerve cracking as a beginner to solve this but with basic mathematics it is easier
jumps = no of iterations
if we have to say "YES" then x1+v1 == x2+v1 @ some point in time ,
that point in time lets say that if we use while loop to loop through each iterations
so here the jumps = the no.of iterations

so our new formula will be 
x1+(v1*jumps) = x2+(v2*jumps)

Now we solve this equation like when we were in class 10th
=> x1+(v1*jumps) = x2+(v2*jumps)
=> (v1*jumps) = x2 + (v2*jumps) - x1
=> (v1*jumps) - (v2*jumps) = x2 - x1
=> jumps= x2-x1 /(v1 - v2)
=> jumps = (x2-x1)%(v1-v2)
'''

def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if (v2>v1 and x2>x1) or (x2<x1 and v2<v1) or (v2==v1):
      return "NO"
    return "YES" if ((x2-x1)%(v1-v2))==0 else "NO"
      
    
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
