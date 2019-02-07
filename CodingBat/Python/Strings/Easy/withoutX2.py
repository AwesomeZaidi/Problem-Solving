
# PROMPT
# Given a string, if one or both of the first 2 chars is 'x', return the string without those 'x' chars,
# and otherwise return the string unchanged. This is a little harder than it looks.


# withoutX2("xHi") → "Hi"
# withoutX2("Hxi") → "Hi"
# withoutX2("Hi") → "Hi"

def withoutX2(word):

    for index, element in enumerate(word[:2]):
        print("e", element)


print(withoutX2("HEllo"))
