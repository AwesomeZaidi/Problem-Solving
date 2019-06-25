def F(n): return list(map( lambda x, f = lambda x, f: int(x <= 1) or (f(x - 1, f) + f(x - 2, f)): f(x, f), range(n)))

# name = 'asim'

# def topLevelFunc(num):
#     return secondFunc(one, two)

# def secondFunc(one, two):
#     int(one <= 1) or (two(one - 1, two) + two(one - 2, f))
# list(map(lambda x, f = lambda x, f: int(x <= 1) or (f(x - 1, f) + f(x - 2, f)): f(x, f), range(n)))

# result = map(topLevelFunc(name), [1,2,3])

# print(result)

print(F(10))