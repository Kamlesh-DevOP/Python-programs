sign=1
st=input('Enter a string: ')
for i in range(len(st)):
    sign*=-1
    if sign==1:
        s=st[i].capitalize()
        print(s,end='')
    elif sign==-1:
        s=st[i]
        print(s,end='')