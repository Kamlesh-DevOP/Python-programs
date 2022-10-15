lst=eval(input('Enter a number: '))
i=0
while i < len(lst):
    if lst[i]==0:
        del lst[i]
        lst.append(0)
    i+=1
print(lst)