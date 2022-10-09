n=int(input('Enter n: '))
l=[2/9]
nr=2
dr=9
for i in range(1,n):
    nr+=3
    dr+=4
    if i%2==1:
        l.append((nr/dr)*-1)
    else:
        l.append(nr/dr)   
print(l)