sum,count=0,0
for i in range(10,1001):
    s=0
    for k in range(1,i):    
        if i%k==0:
            s+=k
    if s==i:
        print(i,end=' ')
        count+=1
        sum+=i
avg=sum/count    
print('\nAverage of these numbers: ',avg)