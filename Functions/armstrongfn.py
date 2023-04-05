def arm(n):
    l=len(str(n))
    temp=n
    s=0
    while temp:
        dig=temp%10
        s+=dig**l
        temp//=10
    if n==s:
        return 1
    else:
        return 0

x=int(input('Enter x: '))
if arm(x):
    print('It is an armstrong number')
else:
    print('It is not an armstrong number')
