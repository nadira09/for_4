# задача 7

def fact(n):
    counter = 1
    factorial = 1
    
    if n == 0:
        yield fact
    
    while n >= counter:
        factorial *= counter
        yield factorial
        counter += 1

for el in fact(5):
    print(el)
