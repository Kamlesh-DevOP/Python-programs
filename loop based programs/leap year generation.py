ll=int(input('Enter lower limit: '))
ul=int(input('Enter upper limit: '))
for i in range(ll,ul+1):
    if i%4==0 and i%100!=0 or i%400==0:
        print(i,end=' ')