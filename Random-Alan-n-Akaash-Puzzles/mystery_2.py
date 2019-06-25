import string
import sys


def puzzle(binary_input, b):
    """
        Create a dictionary values of 1-9-a-z :

        
        Args:       ds      ? type?
                    b       ? type?
        Returns?    ?
    """
    string_values = {char: index for index, char in enumerate(string.printable[:36])}
    # for _, base_36_val in enumerate(string.printable[:36]):
    #     print('base_36_val:', base_36_val)
    # sum( values[d] * b**e for e, d in enumerate(ds[::-1]) )
    sum = 0
    for idx, num in enumerate(binary_input[::-1]):
        print('idx:', idx, 'num:', num)
        current = string_values[num] * b**idx
        sum += current
        print('current:', current)
    
    return sum # wrong

    # return sum(string_values[d] * b**e for e, d in enumerate(ds[::-1]))


if __name__ == '__main__':
    # print('string.printable[:36]:', string.printable[:36])
    print(puzzle(sys.argv[1], int(sys.argv[2])))




