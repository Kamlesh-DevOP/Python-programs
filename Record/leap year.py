year=int(input('Enter an year: '))
if (year%4==0): 
    if year%100!=0:
        print('It is a leap year')
    elif (year%400==0):
        print('It is a leap year')
    else: print('It is not a leap year')
else:
    print('It is not a leap year')
