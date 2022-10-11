index=int(input('Enter index number: '))
value=int(input('Enter value: '))
list=[1,2,3,4,6,7]
l1=list[:index]
l2=[value]
l3=list[index:]
l1=l1+l2+l3
print(l1)