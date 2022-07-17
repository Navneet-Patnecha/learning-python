from errno import ENETDOWN


fname = 'shivank'
lname = 'gautam'
if(fname == 'shivank' and lname == 'gautam'):
    print('yes first name is shivank')
else:
    print('naam galat h bhai')


write_smthng = input('enter a string')
for i in write_smthng:
    if ord(i)%2 == 0:
        print(i)
    
     