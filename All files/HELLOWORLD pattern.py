l='HELLOWORLD'
for i in range(5):
    for k in range(0,i):
        print(' ',end='')
    print(l[i],end=' ')
    end=9-i
    for j in range(i+1,end):
        print(' ',end='')
    print(l[end],end='')
    print()
        