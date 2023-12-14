import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    # Write your code here
    superNum = n

    while len(superNum) > 1:
        tmpNum = 0
        for i in superNum:
            tmpNum += int(i)
        superNum = str(tmpNum)

    return superNum

if __name__ == '__main__':

    n = '123'

    k = len(n)

    print(n)
    print(k)
    result = superDigit(n, k)
    print(result)