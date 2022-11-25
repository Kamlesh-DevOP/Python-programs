st=input('Enter the string: ')
up=low=special=num=0
for i in st:
    if i.isupper():
        up+=1
    elif i.islower():
        low+=1
    elif i.isdigit():
        num+=1
    else:
        special+=1

print('Upper case:',up,'Lower case:',low,'Special characters:',special,'Numbers:',num)
    