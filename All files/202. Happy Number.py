s=int(input('Enter number: '))
l=[]
while s!=1:
    s=str(s)
    sum=0
    for i in s:
        sum+=int(i)**2
    s=sum

    if s in l:
        print('False')
    l+=[s]
print('True')