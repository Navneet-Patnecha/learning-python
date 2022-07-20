from re import I


def greet():
    print('hello world ')
    return 'hi mars'

var = greet()
print(var)


def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

val = factorial(6)
print(val)