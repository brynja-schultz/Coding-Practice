#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if s[-2:] == "PM":
        hour = int(s[0:2])
        if hour < 12:
           hour += 12
        new_time = str(hour) + s[2:8]
        
    elif s[-2:] == "AM":
        hour = s[0:2]
        if int(hour) == 12:
            hour = "00"
        new_time = hour + s[2:8]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
