import string
import sys
import json


def puzzle(ds, b):
    # List comprehension writing to a dictionary.
    v = {element: index for index, element in enumerate(string.printable[:36])}
    print("v:", v)
    return sum(v[element] * b**index for index, element in enumerate(ds[::-1]))

if __name__ == '__main__':
    print(puzzle(sys.argv[1], int(sys.argv[2])))