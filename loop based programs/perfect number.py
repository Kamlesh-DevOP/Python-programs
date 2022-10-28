#perfect number is a number when sum of factors is the number itself
num=int(input('Enter a number: '))
s=0
for i in range(1,num):
    if num%i==0:
        s+=i
if num==s:
    print('It is a perfect number')
else:
    print('Not a perfect number')