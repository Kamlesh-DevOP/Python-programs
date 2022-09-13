#from Shaashu
n=int(input('Enter a number: '))
print('The factors are: ')
i=2
while i<=n:
    if n%i==0:
        f=n/i
        n=n//i
        print(i,end=' ')
    else:
        i+=1
