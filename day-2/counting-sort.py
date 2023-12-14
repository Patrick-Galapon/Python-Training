import math
import os
import random
import re
import sys

#
# A sorting method, the counting sort, does not require comparison. 
# Instead, you create an integer array whose index range covers the 
# entire range of values in your array to sort. Each time a value 
# occurs in the original array, you increment the counter at that index. 
# At the end, run through your counting array, printing the value of 
# each non-zero valued index that number of times
#
# arr = [1,1,3,2,1]
#
# i	arr[i]	result
# 0	1	    [0, 1, 0, 0]
# 1	1	    [0, 2, 0, 0]
# 2	3	    [0, 2, 0, 1]
# 3	2	    [0, 2, 1, 1]
# 4	1	    [0, 3, 1, 1]
# The frequency array is [0, 3, 1, 1]. These values can be used to create the sorted array as well:
# sorted = [1, 1, 1, 2, 3]
#

def countingSort(arr):
    
    sortedArr = []
    for i in range(100):
        sortedArr.append(0)
        
    for i in arr:
        sortedArr[i] += 1
    
    return sortedArr

if __name__ == '__main__':

    arr = [1,1,3,2,1]

    result = countingSort(arr)
    print(result)

