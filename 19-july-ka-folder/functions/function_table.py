from curses.ascii import isupper
from python_functions import greet,factorial
def table(n):
    for i in range(1,11):
        print(n*i)
table(6)

greet()
var = factorial(6)
print(var)

def MyList():
    lst = [1,2,3]
    return lst
print(MyList())







