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
    min_sum = float('inf')
    max_sum = -float('inf')
    # iterates 0, 1, 2, 3, 4
    for i in range(len(arr)):
        # gets sum of list except for current index
        curr_sum = sum(arr[index] for index in range(len(arr)) if index != i)
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum > max_sum:
            max_sum = curr_sum
    
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
