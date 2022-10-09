lst=eval(input('Enter a list: '))
co=ce=0
for i in lst:
    if i%2==0:
        co+=1
    else:
        ce+=1
print(co,'Odd numbers', ce,'Even numbers')


