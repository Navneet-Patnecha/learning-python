from posixpath import split


n = int(input('how many test case : '))
for i in range(n):
    user_input = input('enter a string with operation and operand : ')
    op = user_input.split()
    print(op)
    if op[0] == 'add':
        first_number = int(op[1])
        second_number = int(op[2])
        print(first_number + second_number)

    elif op[0] == 'sub':
        first_number = int(op[1])
        second_number = int(op[2])
        print(first_number - second_number)

    elif op[0] == 'mul':
        first_number = int(op[1])
        second_number = int(op[2])
        print(first_number * second_number)

    elif op[0] == 'div':
        first_number = int(op[1])
        second_number = int(op[2])
        print(first_number / second_number)






    

