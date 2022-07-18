n = int(input('how many times you want to get ascii value : '))
main_string = ''
for i in range(n):
    num = int(input('enter a number between 50 - 150 to get its ascii value : '))
    str = chr(num)
    main_string = str + main_string
print(main_string)
