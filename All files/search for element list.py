l=eval(input('Enter list: '))
x=int(input('Enter element to find: '))
for i in range(len(l)):
    if l[i]==x:
        print(l[i],'is found at',i,'index in this list')