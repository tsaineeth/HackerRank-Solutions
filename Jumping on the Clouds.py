#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(cloudArray):
    dictionary = {0:0, 1:0}
    lengthArray = len(cloudArray)
    minPath = 0
    for i in cloudArray:
        if i==0:
            dictionary[0] += 1
        else:
            dictionary[1] += 1

    if dictionary[1] == 0:
        if lengthArray/2 ==0:
            minPath = int(lengthArray/2 + 1)
            return minPath
        else:
            minPath = int(lengthArray/2)
            return minPath
    else:
        i = 0
        while(i <= lengthArray-2):
            #current = cloudArray[i]
            #next = cloudArray[i+1]
            try:
                nextNext = cloudArray[i+2]
            except IndexError:
                nextNext = 0

            if nextNext == 1:
                minPath += 1
                i += 1
            else:
                minPath += 1
                i += 2

        return minPath

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
