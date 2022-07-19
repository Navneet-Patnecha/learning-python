input_string = input('enter a string : ')
meri_string = input_string.lower()
dict = {}
for i in meri_string:
    
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)

