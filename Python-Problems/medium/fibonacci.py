def fibanacci(num):
    firstNum=1
    secondNum=1
    current=0
    counter = 0
    if num == 1:
        current = firstNum
        return current
    if num == 2:
        current = secondNum
        return current

    while counter < num:
        current = firstNum + secondNum
        firstNum = secondNum
        secondNum = current
        counter+=1

    return current

print(fibanacci(3))

# solution code - better
def gen_fib():
    count = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if count == 0:
        fib = [
    elif count == 1:
        fib = [1]\
    elif count == 2:
        fib = [1,1]
    elif count > 2:
        fib = [1,1]
        while i < (count - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1

    return fib
