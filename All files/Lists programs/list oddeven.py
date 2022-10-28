lst=eval(input('Enter a number: '))
for i in range(len(lst)):
    if lst[i]%2==0:
        lst[i]*=2
    else:
        lst[i]+=5
print(lst)