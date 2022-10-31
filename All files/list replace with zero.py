lst=eval(input('Enter a list: '))
value=int(input('Enter an element to replace with: '))
for i in range(len(lst)):
    if lst[i]==value:
        lst[i]=0
k=0
for j in range(len(lst)):
    if lst[j]==0:
        lst[k],lst[j]=lst[j],lst[k]
        k+=1
print(lst)
#by brilliant madhu