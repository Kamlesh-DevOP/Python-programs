l=eval(input("Enter list: "))
num=int(input('Enter number to search: '))
start=0
stop=len(l)-1
while start<=stop:
    mid=(start+stop)//2
    if num==l[mid]:
        print(num,'found in ',mid+1,'position')
        break
    elif num<l[mid]:
        stop=mid-1
    else:
        start=mid+1
else:
    print(num,'not found in list')

