# Exercise 13:
# Write a function that takes a list and returns a new list that contains
# all the elements of the first list minus duplicates.


def dedupe(x):
  y = []
  for i in x:
      print("i in x = " + str(i))
      if i not in y:
          y.append(i)
          print(y)
  return y

#this one uses sets
def dedupe_v2(x):
    return list(set(x))

# print(dedupe([1,1,11,2,3,4,4,5]))
print(dedupe_v2([1,1,11,2,3,4,4,5]))
