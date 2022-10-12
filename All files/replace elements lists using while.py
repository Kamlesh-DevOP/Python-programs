index=int(input('Enter index number: '))
value=input('Enter value: ')
lst=['a','b','c','d','f']
v=lst[len(lst):]
i=0
L=[]
while i<len(lst):
    if i==index:
        L+=[value]
    else:
        L+=lst[i]
    i+=1
L+=v
print(L)