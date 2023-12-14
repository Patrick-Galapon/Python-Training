import math
import os
import random
import re
import sys

#
# Given an array of integers, where all elements but one occur twice, find the unique element.
#
# EXAMPLE
# a = [1,2,3,4,3,2,1]
# The unique element is 4.
#

def lonelyinteger(a):
    
    counter = 0
    val = 0
    for i in a:

        counter = a.count(i)
        if counter == 1:
            val = i


    return val
        

if __name__ == '__main__':

    a = [1,1,2,2,3,4,4]

    result = lonelyinteger(a)

    print(result)