# 1. FIZZ ARRAY

# Given a number n, create and return a new int array of length n, containing the
# numbers 0, 1, 2, ... n-1. The given n may be 0, in which case just return a length
# 0 array. You do not need a separate if-statement for the length-0 case; the for-loop
# should naturally execute 0 times in that case, so it just works. The syntax to make a
# new int array is: new int[desired_length]   (See also: FizzBuzz Code)


# fizzArray(4) → [0, 1, 2, 3]
# fizzArray(1) → [0]
# fizzArray(10) → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def fizzarray():
    # len = 3
    # string = ''
    # for i in range(10):
    #     if i % 3 == 0:
    #         string = string + 'Fizz'
    #     if i % 5 == 0:
    #         string = string + 'Buzz'

    for num in range(1,21):
        if num % 3 == 0 and num % 5 == 0:
            print('FizzBuzz')
        elif num % 3 == 0:
            print('Fizz')
        elif num % 5 == 0:
            print('Buzz')


# print(fizzarray())

def fizzBuzz(start, end):
    answer = []
    for i in range(start, end):
        # if i is divisable by 3 and 5
            # append fizzBuzz into the list
        # elif i is divisible by 3
            # append fizz into the list
        # elif i is divisible by 5
            # append buzz into the list
        # else
            # append i to the list
        
        # return the list

        pass
    pass

# Given a number n, create and return a new int array of length n,
# containing the numbers 0, 1, 2, ... n-1. The given n may be 0,
# in which case just return a length 0 array. You do not need a separate if-statement
# for the length-0 case; the for-loop should naturally execute 0 times in that case,
# so it just works. The syntax to make a new int array is: new int[desired_length]
# See also: FizzBuzz Code)


# fizzArray(4) → [0, 1, 2, 3]
# fizzArray(1) → [0]
# fizzArray(10) → [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def fizzArray(limit):
    return [num for num in range(limit)]

# print(fizzArray(10))


# Given start and end numbers, return a new array containing the sequence
# of integers from start up to but not including end, so start=5 and end=10
# yields {5, 6, 7, 8, 9}. The end number will be greater or equal to the
# start number. Note that a length-0 array is valid. (See also: FizzBuzz Code)

def fizzArray3(start, end):
    return [num for num in range(start, end)]

print(fizzArray3(5, 10)) # → [5, 6, 7, 8, 9]
print(fizzArray3(11, 18)) # → [11, 12, 13, 14, 15, 16, 17]
print(fizzArray3(1, 3)) # → [1, 2]