'''
54321-15
4321-10
321-7
21-3
1-1
'''
for i in range(5,0,-1):
    sum=0
    for k in range(i,0,-1):
        print(k,end='')
        sum+=k
    print('-',sum)
