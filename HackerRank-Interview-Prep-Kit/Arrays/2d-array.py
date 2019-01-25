'''
    Problem: https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
    Using 2d array, create a list of all the 'hourglass values' and return the largest sum in that list.

    Find a pattern of 3 1 3
    abc
     d
    efg
'''

def max_hour_glass(arr2d):
    '''
        Args:       2d array
        Returns:    largest sum in the list.

        How it works?
            Create a local max variable initially set to 0.
            Create an empty array, hour_glass_sums.
            Create variable, hour_glass_val to get value of current hour glass & store into list.

            Start a for loop through each row of the 2d array.
                Loop through each column in the row.
                Set hour_glass_val = all the hourglass item sum'd up since we know the pattern they exist in.
                Append that value to the list.
            
            Lastly (maybe there's a better way to do this without creating new memory!)
            set max = to the first hour glass sum in the list.
                Loop through each number in the list.
                    Compare it to see if it's larger than the max.
                    If so,
                        Set the max equal to that number.

            Finally, we return the max value.
            
    '''
    # use and change this later
    max = 0
    hour_glass_sums = []
    hour_glass_val = 0
    for row in range(len(arr2d)-2):
        print("row:", row)
        for col in range(len(arr2d)-2):
            print("col:", col)
            hour_glass_val = arr2d[row][col] + arr2d[row][col+1] + arr2d[row][col+2] + arr2d[row+1][col+1] + arr2d[row+2][col] + arr2d[row+2][col+1] + arr2d[row+2][col+2]
            hour_glass_sums.append(hour_glass_val)
    
    # BRUTE FORCE: FIND LARGEST INT IN AN ARRAY
    max = hour_glass_sums[0]
    for num in hour_glass_sums:
        if num > max:
            max = num
        
    return max

use_case_1 = [
    [10, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 10, 0],
    [1 ,1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
    ]

# Donnie's black ass told me to Google enum in python, and range.
print("Max: ", max_hour_glass(use_case_1))

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

# Potential Solutionsaaa
'''
    Brute force of this could be:
        grab [0][0,1,2], [1][1], [2][1,2,3]
        next iterate over one on each item so [1][1,2,3], [1][2], [2][1,2,3]
        next, [0][2,3,4], [1][3], [2][2,3,4]
        final, [0][3,4,5], [1][4], [2][3,4,5]

        then we wan't to move down a column, using [1] and reset our row counts and keep collecting glass sums.

        do this until the row num reaches the total columns in arr - 3, that's when we're at our bottomest row.
'''

# Program Notes! :P
'''
    Google Searches/Links Read Involved in this hot mess:
    how to find a pattern in a 2d array python
    https://www.geeksforgeeks.org/find-orientation-of-a-pattern-in-a-matrix/
    'iterating over a 2d array in python' - https://stackoverflow.com/questions/16548668/iterating-over-a-2-dimensional-python-list
        - lead me to google, 'python zip' - https://docs.python.org/3/library/functions.html#zip
            - which lead me to understand iter - https://docs.python.org/3/library/functions.html#iter
                * which i didn't fully understand
                    - which lead me to google 'python iter explained' - https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration (what looks very basic, good for me!)
                    * What are the most basic definitions of "iterable", "iterator" and "iteration in Python?
                    * Iteration is a general term for taking each item of something, one after another.
                    * In Python, iterable and iterator have specific meanings.
                    * An iterable is an object that has an __iter__ method which returns an iterator, 
                    *  - or which defines a  __getitem__ method that can take sequential indexes starting
                    *  - from zero (and raises an IndexError when the indexes are no longer valid). So an
                    *  - iterable is an object that you can get an iterator from.               
                    * An iterator is an object with a next (Python 2) or __next__ (Python 3) method.
                    - continuing: https://docs.python.org/3/tutorial/classes.html#iterators
                    * The use of iterators pervades and unifies Python. 
                    * Behind the scenes, the for statement calls iter() on the container object.
                    * The function returns an iterator object that defines the method __next__() which accesses elements in the container one at a time.
                    * When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate.
                    * You can call the __next__() method using the next() built-in function; 
                    
                    Example:
                        >>> s = 'abc'
                        >>> it = iter(s)
                        >>> it
                        <iterator object at 0x00A1DB50>
                        >>> next(it)
                        'a'
                        >>> next(it)
                        'b'
                        >>> next(it)
                        'c'
                        >>> next(it)
                        Traceback (most recent call last):
                        File "<stdin>", line 1, in <module>
                            next(it)
                        StopIteration

                    My note: so this bad ass shit takes a string, calls the iter() which returns a an obj 
                                to which we can call the __next__ func on that will access each element in the
                                container one at a time.

                    Turning it into a Class
                    Example: 
                        class Reverse:
                            """Iterator for looping over a sequence backwards."""
                            def __init__(self, data):
                                self.data = data
                                self.index = len(data)

                            def __iter__(self):
                                return self

                            def __next__(self):
                                if self.index == 0:
                                    raise StopIteration
                                self.index = self.index - 1
                                return self.data[self.index]
                        >>>
                        >>> rev = Reverse('spam')
                        >>> iter(rev)
                        <__main__.Reverse object at 0x00A1DB50>
                        >>> for char in rev:
                        ...     print(char)
                        ...
                        m
                        a
                        p
                        s

                    - Then i saw Generators below that, an easy tool to create iterators.
                    - They are written like regular functions but use the yield statement whenever they want to return data.
                    
                    Example:
            
                        def reverse(data):
                            for index in range(len(data)-1, -1, -1):
                                yield data[index]
                        >>>
                        >>> for char in reverse('golf'):
                        ...     print(char)
                        ...
                        f
                        l
                        o
                        g
                    - generators are compact because __iter__() and __next__() methods are created automatically.
                    - Another key feature is that the local variables and execution state are automatically saved between calls.
                    - This made the function easier to write and much more clear than an approach using instance variables like self.index and self.data.
                    - In addition to automatic method creation and saving program state, when generators terminate, they automatically raise StopIteration.

                    Next: Generator Expressions
                        - and i wasn't really going to bother getting too deep into this, looked complicated.
            
            Now, I understand iterables (obj with __iter__  method that returns an 'iterator') and iterators(obj next that access each element in container one at a time.)  (iters) in Python.
            - should learn this next: Iterator Types - https://docs.python.org/dev/library/stdtypes.html#iterator-types   
            - Then, get more advanced with iterators in functional programming - https://docs.python.org/dev/howto/functional.html#iterators
            
            Continuing, with zip - https://docs.python.org/3/library/functions.html#zip

            So zip:
             - Returns an iterator of tuples.
             - The iterator stops when the shortest input iterable is exhausted. 

             Doc gives us this code example:
             def zip(*iterables):
                # zip('ABCD', 'xy') --> Ax By
                sentinel = object()
                iterators = [iter(it) for it in iterables]
                while iterators:
                    result = []
                    for it in iterators:
                        elem = next(it, sentinel)
                        if elem is sentinel:
                            return
                        result.append(elem)
                    yield tuple(result)
            
            the for loop list comprehension threw me off, so did the *parameter
            - * is simply used to pass a variable number of arguments to a function

            my next zip resource (medium can be a go to)
            https://medium.com/@happymishra66/zip-in-python-48cb4f70d013

            zip takes n number of iterables and returns list of tuples.
            Easy Code Example!
                list_a = [1, 2, 3, 4, 5]
                list_b = ['a', 'b', 'c', 'd', 'e']

                zipped_list = zip(list_a, list_b)

                print zipped_list # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
    Back to the drawing board on how we can do this without zip...
    Maybe a nested for loop, that SOF didn't make much sense to me afterall... so let's try another source.

    So i'm on my way with this solution but my for loop is broken.
    I'm getting in my console:
        TypeError: 'int' object is not iterable
    on this line:
        for row in len(arr2d)-3:
    
    I want to say range will solve my problem here, let's learn about range in Python 3 first.
    
    - range is actually an immutable sequence type.

'''         