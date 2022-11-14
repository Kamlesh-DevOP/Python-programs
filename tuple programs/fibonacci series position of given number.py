t=()
x=int(input('Enter number to be searched: '))
a=-1
b=1
c=0
while c<x:
    c=a+b
    a=b
    b=c
    t+=c,
print(t)
print(x,'is present in',len(t),'position')