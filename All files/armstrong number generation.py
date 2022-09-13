#eg. 1634. 1^4+6^4+3^4+4^4=1634
ll=int(input('Enter lower limit: '))
ul=int(input('Enter upper limit: '))
for i in range(ll,ul):
    n=str(i)
    p=len(n)
    s=0
    for k in n:
        s+=int(k)**p
    if i==s:
        print(i)
