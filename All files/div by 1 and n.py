#Write a python program to print every integer between 1 and n divisible by m.
m=int(input('Enter the number m : '))
n=int(input('Enter the number n : '))
for i in range(1,n+1):
    if i%m==0:
        print(i)
print('These numbers are divisible by',m,'between 1 and',n )