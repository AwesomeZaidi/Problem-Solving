# Hacker Rank problem - https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# Solution: Asim Zaidi
# 01/05/19
# Rotate an array 2 indeces to the left.

def rotLeft(a, k):
    '''
        Args:
            - a, number of integers in array.
            - n, number of rotations to perform.
            - k, array
        Returns:
            - arr, size of a, elements rotated b*2 indeces to the left.
    '''
    return a[k:] + a[:k]
    # n, k = map(int, input().strip().split(' '))
    # a = map(int, input().strip().split(' '))
    # answer = array_left_rotation(a, n, k);
    # print(*answer, sep=' ')

useCase1 = rotLeft([1,2,3], 3)
# useCase2 = rotLeft(4,4)
# useCase3 = rotLeft(5,10)

print("useCase1:", useCase1)
# print("useCase2:", useCase2)
# print("useCase2:", useCase3)