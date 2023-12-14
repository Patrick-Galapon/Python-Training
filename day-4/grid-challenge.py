import math
import os
import random
import re
import sys

#
# Given a square grid of characters in the range ascii[a-z], rearrange elements 
# of each row alphabetically, ascending. Determine if the columns are also in 
# ascending alphabetical order, top to bottom. Return YES if they are or NO 
# if they are not.
#
# EXAMPLE
# grid = ['abc','ade','efg']
#
# The rows are already in alphabetical order. The columns a a e, b d f and c e g 
# are also in alphabetical order, so the answer would be YES. Only elements within 
# the same row can be rearranged. They cannot be moved to a different row.
#

def gridChallenge(grid):

    val = 'YES'    
    newGrid = []
    gridLength = 0
    for i in grid:
        tmpGrid = []
        for j in i:
            tmpGrid.append(j)
        tmpGrid.sort()
        gridLength = len(tmpGrid)
        
        tmpString = ''
        for x in tmpGrid:
            tmpString += x
        
        newGrid.append(tmpString)
    
    finalGrid = []
    for i in range(gridLength):
        tmpArray = []
        for j in newGrid:
            tmpArray.append(j[i])
        finalGrid.append(tmpArray)
    

    for i in finalGrid:
        if i != sorted(i):
            val = 'NO'                
                
    return val
        
            

if __name__ == '__main__':

    grid = ['abc','ade','efg']

    result = gridChallenge(grid)
    print(result)

