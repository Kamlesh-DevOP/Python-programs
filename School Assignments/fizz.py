for k in range(1,101):
    num=int(input('Enter a number: '))
    if num>100:
        print('Invalid number ')
    elif num%3==0:
        print('Fizz')
#elif vs if