
# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".


# helloName("Bob") → "Hello Bob!"
# helloName("Alice") → "Hello Alice!"
# helloName("X") → "Hello X!"

def helloName(name):
    sentence = "Hello " + name + "!"
    return sentence

useCase1 = "Bob"
useCase1 = "Alice"


print(helloName(useCase1))