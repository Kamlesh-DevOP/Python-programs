n=int(input('Enter the end value: '))
s=0
count=0
for i in range(1,n+1):
    s+=i
    count+=1
print('Average of first',n,'numbers is',s/count)