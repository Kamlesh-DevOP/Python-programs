ll=int(input('Enter lower limit: '))
ul=int(input('Enter upper limit: '))
for i in range(ll,ul+1):
    if i<=1:
        continue
    for k in range(2,i):
        if i%k==0:
            break
    else:
        print(i, end=' ')