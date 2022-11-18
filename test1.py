#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'findModeCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER num
#  2. INTEGER base
#  3. STRING start
#
def findNextNumber(prev, base):
    prev = list(prev)
    for i in range(len(prev)):
        prev[i] = int(prev[i])
    prev[-1] = prev[-1]+1
    for i in range(len(prev)-1, -1, -1):
        if (prev[i] == base):
            prev[i] = 0
            if (i-1 < 0):
                prev.insert(0, 1)
            else:
                prev[i-1] = prev[i-1]+1
    return str(prev).replace("[", "").replace("]", "").replace(",", "").replace(" ", "")
def findModeCount(num, base, start):
    count = 1
    generated = [str(start)]
    while count < num:
        generated.append(findNextNumber(generated[-1], base))
        count+=1
    print(generated)
    dictionary = {
        0: 0,
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
        7: 0,
    }
    for generate in generated:
        for character in str(generate):
            dictionary[int(character)]+=1
    most = 0
    for value in dictionary.keys():
        if (dictionary[value] > dictionary[most]):
            most = value
    return dictionary[most]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # num = int(input().strip())
    #
    # base = int(input().strip())
    #
    # start = input()
    #
    # result = findModeCount(num, base, start)
    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
    findNextNumber("7", 8)
    print(findModeCount(15, 8, 2))
