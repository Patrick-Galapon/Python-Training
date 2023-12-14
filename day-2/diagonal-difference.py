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
    val = 0
    counterA = 0
    counterB = 0
    indexA = 0
    indexB = len(arr) - 1
    
    for i in arr:

        counterA += i[indexA]
        counterB += i[indexB]
        indexA += 1
        indexB -= 1
    
    arrCounter = [counterA, counterB]
    return max(arrCounter) - min(arrCounter)

    
if __name__ == '__main__':
    
    arr = [[2,4,6],[3,5,7],[8,0,-12]]

    result = diagonalDifference(arr)
    print(result)
