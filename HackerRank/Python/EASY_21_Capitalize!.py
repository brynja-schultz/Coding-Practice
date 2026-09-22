#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # split string into words
    words = s.split(" ")
    for i in range(len(words)):
        # if first letter is lower case, make uppercase
        if words[i] and words[i][0].isalpha() and words[i][0].islower():
            words[i] = words[i][0].upper() + words[i][1:]
    string = " ".join(words)
    return string
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
