#
# Given an array of  distinct integers, transform the array into a zig zag sequence 
# by permuting the array elements. A sequence will be called a zig zag sequence if 
# the first  elements in the sequence are in increasing order and the last k
# elements are in decreasing order, where k-(n+1). You need to find the lexicographically 
# smallest zig zag sequence of the given array.
#
# EXAMPLE
# a = [2,3,5,1,4]
# Now if we permute the array as [1,4,3,5,2], the result is a zig zag sequence.
# Debug the given function findZigZagSequence to return the appropriate zig zag 
# sequence for the given input array.\
#

def findZigZagSequence(a, n):
    a.sort()
    mid = int((n - 1)/2)
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)