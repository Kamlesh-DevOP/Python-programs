sum=0
count=0
for i in range(10,51):
    if i<=1:
        continue
    for k in range(2,i):
        if i%k==0:
            break
    else:
        print(i, end=' ')
        count+=1
        sum+=i
print('\nAverage is',sum/count)