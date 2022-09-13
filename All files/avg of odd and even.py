#from Ajeetha
counteven=0
countodd=0
sumeven=0
sumodd=0
while True:
    n=int(input('Enter the number: '))
    if n%2==0:
        counteven+=1
        sumeven+=n
    if n%2==0:
        countodd+=1
        sumodd+=n
    if n==-123:
        break
avgeven=sumeven/counteven
avgodd=sumodd/countodd
print('Average of odd numbers is',avgodd,'\nAverage of even numbers is',avgeven)
