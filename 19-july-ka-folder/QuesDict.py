input_string = input('enter a string : ')
dict = {}
for i in input_string:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)


    
