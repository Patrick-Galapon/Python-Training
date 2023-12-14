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
    
    # Write your code here
    char_shift = {}
    for ch in s:
        if ord('a') <= ord(ch) <= ord('z'):
            shift_by = (ord(ch)-ord('a')+k) % 26
            char_shift[ch] = chr(ord('a') + shift_by)
        elif ord('A') <= ord(ch) <= ord('Z'):
            shift_by = (ord(ch)-ord('A')+k) % 26
            char_shift[ch] = chr(ord('A') + shift_by)
    
    return "".join([char_shift.get(ch, ch) for ch in s])

        
if __name__ == '__main__':

    s = 'There''s-a-stream-waiting-in-the-sky'

    k = 3

    result = caesarCipher(s, k)
    print(result)
