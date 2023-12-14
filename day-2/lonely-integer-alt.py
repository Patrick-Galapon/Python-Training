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
    
    for value in a:
        if(a.count(value) == 1):
            return(value)        

if __name__ == '__main__':

    a = [11,20,11,20,99,20,11]

    result = lonelyinteger(a)

    print(result)