import string
import sys


def puzzle(ds, b):
    v = {c: i for i, c in enumerate(string.printable[:36])}
    return sum(v[d] * b**e for e, d in enumerate(ds[::-1]))


if __name__ == '__main__':
    print(puzzle(sys.argv[1], int(sys.argv[2])))