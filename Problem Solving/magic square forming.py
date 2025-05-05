#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def generate_permutations(nums, start, result):
    if start == len(nums):
        result.append(nums[:])
        return
    for i in range(start, len(nums)):
        nums[start], nums[i] = nums[i], nums[start]
        generate_permutations(nums, start + 1, result)
        nums[start], nums[i] = nums[i], nums[start]  # backtrack

def to_matrix(lst):
    return [lst[0:3], lst[3:6], lst[6:9]]

def is_magic(square):
    # Check rows, columns and diagonals
    for i in range(3):
        if sum(square[i]) != 15:
            return False
        if sum([square[j][i] for j in range(3)]) != 15:
            return False
    if (square[0][0] + square[1][1] + square[2][2]) != 15:
        return False
    if (square[0][2] + square[1][1] + square[2][0]) != 15:
        return False
    return True

def calculate_cost(matrix1, matrix2):
    cost = 0
    for i in range(3):
        for j in range(3):
            cost += abs(matrix1[i][j] - matrix2[i][j])
    return cost

def formingMagicSquare(s):
    # Write your code here
    perms = []
    generate_permutations([1,2,3,4,5,6,7,8,9], 0, perms)
    
    # Filter valid magic squares
    magic_squares = [to_matrix(p) for p in perms if is_magic(to_matrix(p))]
    
    # Finding magic square with lowest cost
    min_cost = float('inf')
    best_square = None
    for square in magic_squares:
        cost = calculate_cost(s, square)
        if cost < min_cost:
            min_cost = cost
            best_square = square
    
    return min_cost
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
