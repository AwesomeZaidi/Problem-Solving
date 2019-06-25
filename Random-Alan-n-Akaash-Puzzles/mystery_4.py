# print(", \n".join(map(lambda px, n: px + str(n), [s for _ in ns], ns)))

word = 'asim'
nums = [3, 2, "b", 4]

# print(", \n".join(map(lambda px, n: px + str(n), [word for _ in nums], nums) ))
'<---------------------------Difference---------------------------------->'

def addition(n):
    return word + str(n)


result = list(map(addition, nums))

print(', \n'.join(result))