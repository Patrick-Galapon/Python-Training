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
    
    sorted_arr = sorted(arr)
    min_sum = sum(sorted_arr[:-1])
    max_sum = sum(sorted_arr[1:])
    
    print(min_sum, max_sum)        

if __name__ == '__main__':

    arr = [2, 8, 6, 7, 4]

    miniMaxSum(arr)