from itertools import count


s=0
count=0
while True:
    n=int(input('Enter the number: '))
    if n==-123:
        break
    s+=n
    count+=1
avg=s/count
print('Average of the numbers is:',avg)