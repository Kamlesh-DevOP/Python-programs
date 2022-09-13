ll=int(input('Enter lower limit: '))
ul=int(input('Enter upper limit: '))
count=0
for i in range(ll,ul+1):
    if i==int(str(i)[::-1]):
        count+=1
        print(i,end=' ')
print('\nCount: ',count)