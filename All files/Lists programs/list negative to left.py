lst=eval(input('Enter a list: '))
l1,l2=[],[]
for i in lst:
    if i<0:
        l1+=[i]
    elif i>0:
        l2+=[i]
l1+=l2
print(l1)