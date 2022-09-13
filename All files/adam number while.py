ll=int(input('Enter lower limit: '))
ul=int(input('Enter upper limit: '))
k=ll
while k<=ul:
    r=int(str(k)[::-1])
    if k**2==int(str(r**2)[::-1]):
        print(k)
    k+=1