ll=int(input('Enter lower limit: '))
ul=int(input('Enter upper limit: '))
for i in range(ll,ul):
    s=0
    for k in range(1,i):    
        if i%k==0:
            s+=k
    if s==i:
        print(i)