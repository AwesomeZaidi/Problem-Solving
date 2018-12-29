#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    m1 = set(s1)
    m2 = set(s2)
    if set.intersection(m1,m2):
        return "YES"
    return "NO"
if __name__ == '__main__':
    useCase1Solution = twoStrings("hello", "world")
    useCase2Solution = twoStrings("hi", "world")

    print(useCase1Solution)
    print(useCase2Solution)