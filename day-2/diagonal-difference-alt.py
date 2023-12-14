#!/bin/python3

import math
import os
import random
import re
import sys
import math

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):

    # Write your code here
    n = len(arr)
    
    pd = 0
    sd = 0
    
    for i in range(n):
        pd += arr[i][i]
        sd += arr[i][(n-1) - i]
    
    return(abs(pd - sd))
    
if __name__ == '__main__':
    
    arr = [[2,4,6],[3,5,7],[8,0,-12]]

    result = diagonalDifference(arr)
    print(result)
