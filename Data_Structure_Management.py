#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    l=len(arr[0])
    lfin=l-2
    aux=0
    suma=-9999999999

    for i in range(lfin):
        for j in range(lfin):
            aux=(arr[i][j])+(arr[i][j+1])+(arr[i][j+2])+(arr[i+1][j+1])+(arr[i+2][j])+(arr[i+2][j+1])+(arr[i+2][j+2])
            if aux>suma:
                suma=aux
    return(suma)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
