#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'maxSubarrayValue' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarrayValue(arr):
    evenArr = []
    oddArr = []
    for el in arr:
        if el%2==0:
            evenArr.append(el)
        else:
            oddArr.append(el)
    evens = sum(evenArr)
    odds = sum(oddArr)
    result = (evens - odds) ** 2
    if 1 <= result <= 10**5:
        return result
    else:
        raise "Error between 1 and " + str(10**5)
        exit()

if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = []
    for _ in range(arr_count):
        arr_item = int(input().strip())
        if -10**4 <= arr_item <= 10**4:
            arr.append(arr_item)
        else:
            raise "Between " + str(-10**4) + " - " + str(10**4)

    result = maxSubarrayValue(arr)
    print(result)