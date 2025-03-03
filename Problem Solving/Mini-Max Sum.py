#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    new_arr = arr.copy()
    new_arr_1 = []
    
    for i in range(len(arr)):
        if arr[i] in new_arr:
            new_arr.remove(arr[i])
            new_arr_1.append(sum(new_arr))
            new_arr.append(arr[i])
    
    print( min(new_arr_1) , max(new_arr_1))
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
