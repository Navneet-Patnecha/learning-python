lst = []
while True:
    commands = input() # push 3, pop 3, stop
    op, value = commands.split() # don;t use the op, value but use command as list.
    if commands == 'stop':
        break
    elif commands == 'push':
        lst.append(value)
    elif commands == 'pop':
        index_of_value = lst.index(value)
        lst.pop(index_of_value)
    else:
        print('Invalid command')
        continue


             


    