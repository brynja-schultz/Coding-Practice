#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    num_pos = 0
    num_neg = 0
    num_zero = 0

    for val in arr:
        if val > 0:
            num_pos += 1
        elif val < 0:
            num_neg += 1
        else:
            num_zero += 1

    total = len(arr)
    
    pos_ratio = num_pos / total
    neg_ratio = num_neg / total
    zero_ratio = num_zero / total
    
    print(f"{pos_ratio:.6f}")
    print(f"{neg_ratio:.6f}")
    print(f"{zero_ratio:.6f}")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
