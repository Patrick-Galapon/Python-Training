import math
import os
import random
import re
import sys

#
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.  Scale to six
# decimal places.
# 
# Example
# arr = [1, 1, 0, -1, -1]
# 
# Output
# 0.400000 (2 positive integers out of 5 elements)
# 0.400000 (2 negative integers out of 5 elements)
# 0.200000 (1 zero integer out of 5 elements)
#

def plusMinus(arr):
    
    positiveNum = 0
    negativeNum = 0
    zeroNum = 0
    
    for i in arr:
        if i > 0:
            positiveNum += 1
        elif i < 0:
            negativeNum += 1
        else:
            zeroNum += 1
    
    print('{0:.6f}'.format(positiveNum / len(arr)))
    print('{0:.6f}'.format(negativeNum / len(arr)))
    print('{0:.6f}'.format(zeroNum / len(arr)))
        

if __name__ == '__main__':
    #n = int(input().strip())

    arr = [1, 1, 0, -1, -1]

    plusMinus(arr)