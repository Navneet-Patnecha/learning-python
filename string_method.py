from random import random


first_name = 'navneet'
last_name = 'patnecha'

print(first_name.upper())
update_fname = first_name.capitalize()
print(update_fname , first_name)
first_name = first_name.capitalize()
print(first_name)
print(first_name.islower())
print(first_name.count('a'))
lst = [1,2,3,4,'hello', ['1','2','3']]

print(lst)
random_number_list = [10,20,12,45,67,89,12,34,56,78,90]
random_number_list.sort()
print(random_number_list)
random_number_list.sort(reverse=True)
print(random_number_list)
random_number_list.append('hello world')
print(random_number_list)
n = 'navneet'
ls = list(n)
ls.sort()
print(ls)
print(lst[4][1])
a = [12 , 3, 5,]
b = [3,4,5]
print(a+b)
a.append(b)
print(a)
a.extend(b)
print(a)
