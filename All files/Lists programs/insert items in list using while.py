lst=eval(input('Enter a list: '))
index=int(input('Enter index number: '))
value=input('Enter value: ')
le=len(lst)
lst+=[value]
i=0
while i<len(lst)-index-1:
    lst[le-i],lst[le-i-1]=lst[le-i-1],lst[le-i]
    i+=1
print(lst)
#idea by ajee