l1=eval(input('Enter a list: '))
l2=eval(input('Enter a list: '))
common=[]
for i in l1:
    for k in l2:
        if i==k:
            common.append(i)
print(common)
