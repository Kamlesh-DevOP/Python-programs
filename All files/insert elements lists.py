from ast import Index


index=int(input('Enter index number: '))
value=input('Enter value: ')
lst=['a','b','c','d','f']
i=0
L=[]
while i<index:
    L+=lst[i]
    i+=1
L+=[value]
L+=lst[index:]
print(L)