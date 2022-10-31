l=eval(input('Enter a list: '))
if len(l)%2==1:
    mid=(len(l)//2)+1
else:
    mid=int(len(l)/2)
print(max(l[mid:]))