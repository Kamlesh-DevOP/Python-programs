print('check if 1st list is the superset of the 2nd list')
l1=eval(input('Enter list 1: '))
l2=eval(input('Enter list 2: '))
for i in l2:
    if i not in l1:
        flag=0
    else: 
        flag=1
if flag==1:
    print('Yes,',l1,'is the superset of',l2)
else:
    print('No',l1,'is not the superset of',l2)
