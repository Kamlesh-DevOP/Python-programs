counteven=0
countodd=0
sumeven=0
sumodd=0
for i in range(15):
    n=int(input('Enter the number: '))
    if n%2==0:
        counteven+=1
        sumeven+=n
    if n%2!=0:
        countodd+=1
        sumodd+=n
avgeven=sumeven/counteven
avgodd=sumodd/countodd
print('Sum of odd numbers is',sumodd,'\tAverage of odd numbers is',avgodd,
'\nSum of even numbers is',sumeven,'\tAverage of even numbers is',avgeven)
