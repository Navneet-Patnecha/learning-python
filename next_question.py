n = int(input( ))
my_dict = {
    'str' : [],
    'int' : [],
    'float' : [],

  

}
for i in range(n):
    data_type = input()
    value = input()
    if data_type == 'str':
        my_dict['str'].append(value)
    elif data_type == 'int':
        my_dict['int'].append(int(value))
    elif data_type == 'float':
        my_dict['float'].append(float(value))
    else:
        if data_type not in my_dict:
            my_dict[data_type] = data_type
            my_dict[value] = input()
print(my_dict)
    

    

