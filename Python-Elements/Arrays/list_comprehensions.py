# Python provides a feature called list comprehension that is a succinct way to create lists. A
# list comprehension consists of (1.) an input sequence, (2.) an iterator over the input sequence,
# (3.) a logical condition over the iterator (this is optional), and (4.) an expression that yields
# the elements of the derived list. For example, [x**2 for a in range(6)] yields [1, 4, 9,
# 16, 25], and [x**2 for a in range(6) if x % 2 == 0] yields [4,16].

# Although list comprehensions can always be rewritten using map(), filter(), and lambdas, they are clearer to read, in large part because they do not need lambdas.
# List comprehension supports multiple levels of looping. This can be used to create the
# product of sets, e.g., if A = [1, 3, 5] and B = [’a’, ’b’], then [(x, y) for x in A for y
# in B] creates [(1, ’a’), (1, ’b’), (3, ’a’), (3, ’b’), (5, ’a’), (5, ’b’)]. It can
# also be used to convert a 2D list to a 1D list, e.g., if M = [[’a’, ’b’, ’c’], [’d’, ’e’,
# ’f’]], x for row in M for x in row creates [’a’, ’b’, ’c’, ’d’, ’e’, ’f’]. Two levels of looping also allow for iterating over each entry in a 2D list, e.g., if A = [[1,
# 2, 3], [4, 5, 6]] then [[x**2 for x in row] for row in M] yields [[1, 4, 9], [16,
# 25, 36]].
# As a general rule, it is best to avoid more than two nested comprehensions, and use
# conventional nested for loops—the indentation makes it easier to read the program.
# Finally, sets and dictionaries also support list comprehensions, with the same benefits.

print([x**x for x in range(7) if x % 2 == 0])

# print([x**2 for x in range(7) if x % 2 == 0])