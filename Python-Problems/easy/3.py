# a = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(b[2:9:3])
# newList=[]
c = list(set(a).intersection(set(b)))

for i in a:
    for j in b:
        if i == j:
            if i not in newList:
                newList.append(i)

print(c)
# palindrom string reversal technique
wrd=input("Please enter a word: ")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")

# using loops
# def reverse(word):
	# x = ''
	# for i in range(len(word)):
	# 	x += word[len(word)-1-i]
	# 	return x
#
# word = input('give me a word:\n')
# x = reverse(word)
# if x == word:
# 	print('This is a Palindrome')
# else:
# 	print('This is NOT a Palindrome')
# list comprehensions
# years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
# ages = [2014 - year for year in years_of_birth]
# print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
# equil to
# combs = []
# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             combs.append((x, y))
#
# print(combs)
#
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# list = [i for i in a if i % 2 == 0]
# print(list)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print([list(set(a).intersection(set(b)))])
