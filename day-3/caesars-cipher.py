import math
import os
import random
import re
import sys

#
# Julius Caesar protected his confidential information by encrypting it 
# using a cipher. Caesar's cipher shifts each letter by a number of letters. 
# If the shift takes you past the end of the alphabet, just rotate back to 
# the front of the alphabet. In the case of a rotation by 3, w, x, y and z 
# would map to z, a, b and c.
#
# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
#
# EXAMPLE
# s = There's-a-stream-waiting-in-the-sky
# k = 3
#
# The alphabet is rotated by 3, matching the mapping above. The encrypted string is:
# Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb
#

def caesarCipher(s, k):
    
    newString = ''

    for i in s:
        
        newChr = ''
        if (i.isupper() is False and ord(i)+k > ord('z')) or (i.isupper() and ord(i)+k > ord('Z')):
            if i.isalpha():
                newChr = chr(ord(i) + k)
                if i.isupper():
                    while ord(newChr) > ord('Z'):
                        newChr = chr(ord(newChr)-26)
                else:
                    while ord(newChr) > ord('z'):
                        newChr = chr(ord(newChr)-26)
                newString += newChr
            else:
                newString += i
        else:
            if i.isalpha():
                newString += chr(ord(i)+k)
            else:
                newString += i

    return newString

        
if __name__ == '__main__':

    s = 'There''s-a-stream-waiting-in-the-sky'

    k = 3

    result = caesarCipher(s, k)
    print(result)
