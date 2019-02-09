#!python3


def square_up(n):
    """Simple test cases in docstring
    >>> square_up(2)
    [0, 1, 2, 1]
    >>> square_up(3)
    [0, 0, 1, 0, 2, 1, 3, 2, 1]
    >>> square_up(4)
    [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]
    >>> square_up(5)
    [0, 0, 0, 0, 1, 0, 0, 0, 2, 1, 0, 0, 3, 2, 1, 0, 4, 3, 2, 1, 5, 4, 3, 2, 1]
    """

    # a = []

    # # Loop in 2 dimensions, as a matrix (row i, column j)
    # for i in range(n):
    #     for j in range(n):
    #         # Upper left triangle
    #         # if i+j < n-1:
    #         #     a.append(0)
    #         # # Lower right triangle
    #         # else:
    #         #     a.append(n-j)

    #         # Equivalent tertiary expression
    #         # a.append(0 if i+j < n-1 else n-j)
    # return a

    # # Equivalent list comprehension
    return [0 if i+j < n-1 else n-j for i in range(n) for j in range(n)]


if __name__ == '__main__':
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    print(square_up(n))

    # Run docstring tests
    import doctest
    doctest.testmod()