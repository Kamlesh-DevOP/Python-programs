l=[]
x=int(input('Enter any number(-1 to end): '))
l.append(x)
while x:
    x=int(input('Enter any number: '))
    if x==-1:
        break
    l.append(x)
print(l)