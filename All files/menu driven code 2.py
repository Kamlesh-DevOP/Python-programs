q=int(input('What do you want to do? 1 for sum of first n numbers 2 for multiplication table 3 for exit '))
if q==1:
    n=int(input('How many numbers? '))
    sum=0
    for i in range(1,n+1):
        sum+=i
    print('Sum is : ', sum)

elif q==2:
    n=int(input('Multiples of what? '))
    m=int(input('How many multiples? '))
    for i in range(1,m+1):
        t=n*i
        print(t)
 
elif q==3:
    quit()