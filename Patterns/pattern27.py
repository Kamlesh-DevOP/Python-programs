'''
1-1
12-3
123-6
'''
n=int(input('Enter n: '))
for i in range(1,n+1):
    sum=0
    for j in range(1,i+1):
        sum+=j
        print(j,end='')
    print('-',sum,sep='')