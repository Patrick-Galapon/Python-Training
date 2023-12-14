import math
import os
import random
import re
import sys
import datetime
from datetime import timedelta

#
# Given a time in -hour AM/PM format, convert it to military (24-hour) time.
#
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
#
# Example
# s = '12:01:00PM' returns '12:01:00'
# s = '12:01:00AM' returns '00:01:00'
#

def timeConversion(s):

    ampm = s[-2:]

    if ampm == 'AM':
        if s[:2] == '12':
            s = '00' + s[2:]

    tmpDatetime = datetime.datetime.strptime(s, '%H:%M:%S%p')
    
    if ampm == 'PM':
        if s[:2] != '12':
            tmpDatetime += timedelta(hours=12)
    
    return tmpDatetime.strftime('%H:%M:%S')
    

if __name__ == '__main__':

    s = '05:43:17AM'

    result = timeConversion(s)

    print(result)