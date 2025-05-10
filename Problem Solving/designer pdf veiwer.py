#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'designerPdfViewer' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h
#  2. STRING word
#

def designerPdfViewer(h, word):
    # Write your code here
    # print(h)
    alphabets = []
    for i in range(97,123):
      alphabets.append(chr(i))
    # print(alphabets)
    
    nw_dict = dict(zip(alphabets,h))
    # print(nw_dict)
    
    # print(word)
    word = word.strip()
    # print(word)
    
    word_ls = list(word)
    # print(word_ls)
    
    custom_word_num_ls = []
    
    for i in word_ls:
      for key, value in nw_dict.items():
        if key ==i:
          custom_word_num_ls.append(value)
    
    # print(f"for the word {word}, we have num list as {custom_word_num_ls}")
    max_len = max(custom_word_num_ls)
    len_word_num_ls = len(custom_word_num_ls)
    
    return max_len*len_word_num_ls
    
      
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
