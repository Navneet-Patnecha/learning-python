n = int(input(' enter a number : '))
total_add = 0
total_mul = 1
for i in range(n):
    op = input('please input operation string ')
    op_lst = op.split()
    if op_lst[0] == 'add':
        for j in range(1,len(op_lst)):
            total_add = total_add + int(op_lst[j])
        print(total_add)
        total_add = 0
    elif op_lst[0] == 'mul':
        for j in total_mul*int(op_lst[j])
        print(total_mul)
        total_mul = 1
    




