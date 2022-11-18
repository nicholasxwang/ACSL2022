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
conversions = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15,
    "G": 16,
}
unconversions = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
    16: "G",
}
nextLetter = {
    "A": "B",
    "B": "C",
    "C": "D",
    "D": "E",
    "E": "F",
    "F": "G",
}

def findNextNumber(prev, base):
    prev = list(prev)
    for i in range(len(prev)):
        if prev[i] not in conversions.keys():
            prev[i] = int(prev[i])
        else:
            prev[i] = conversions[prev[i]]
    prev[-1] = prev[-1]+1
    for i in range(len(prev)-1, -1, -1):
        if (prev[i] == base):
            prev[i] = 0
            if (i-1 < 0):
                prev.insert(0, 1)
            else:
                prev[i-1] = prev[i-1]+1
    # return str(prev).replace("[", "").replace("]", "").replace(",", "").replace(" ", "")
    return_string = ""
    for i in prev:
        if (i < 10):
            return_string += str(i)
        else:
            return_string += unconversions[i]
    return return_string
def findModeCount(num, base, start):
    count = 1
    generated = [str(start)]
    while count < num:
        generated.append(findNextNumber(generated[-1], base))
        count+=1
    #print(generated)
    dictionary = {}
    for i in range(0, base):
        dictionary[i] = 0
    for generate in generated:
        for character in str(generate):
            # dictionary[int(character)]+=1
            if character not in conversions.keys(): #not letter
                dictionary[int(character)]+=1
            else: #letter
                dictionary[conversions[character]]+=1

    most = 0
    for value in dictionary.keys():
        if (dictionary[value] > dictionary[most]):
            most = value
    return dictionary[most]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num = int(input().strip())

    base = int(input().strip())

    start = input()

    result = findModeCount(num, base, start)

    fptr.write(str(result) + '\n')

    fptr.close()
    # findNextNumber("7", 8)
    # print(findModeCount(20, 12, "9AB"))
