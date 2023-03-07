n=7
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(i!=0):
        a[i].append(1)

for i in range(len(a)):
    for k in range(len(a)-i-1):
        print('  ',end=' ')
    for j in range(len(a[i])):
        if len(str(a[i][j]))==1:
            print('0'+str(a[i][j]),end='    ')
        else:
            print(a[i][j],end='    ',)
    print()
#pascal triangle