import math
import os
import random
import re
import sys

#
# Given five positive integers, find the minimum and maximum values that can be calculated by 
# summing exactly four of the five integers. Then print the respective minimum and maximum values 
# as a single line of two space-separated long integers.
# 
# Example
# arr = [1,3,5,7,9]
#

def miniMaxSum(arr):
    
    sumArr = []
    tmpSum = 0
    index = 0

    for index in range(len(arr)):
        # print(index)
        for i in range(len(arr)):
            # print(i)
            if i == index:
                continue
            else:
                tmpSum += arr[i]
        sumArr.append(tmpSum)
        tmpSum = 0    
    
    print(str(min(sumArr)) + ' ' + str(max(sumArr)))
        

if __name__ == '__main__':

    arr = [2, 8, 6, 7, 4]

    miniMaxSum(arr)