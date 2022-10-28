#buzz number is divisible by 7 or ending with 7
a=int(input('Enter a number: '))
if a%7==0 or a%10==7:
    print('This is a buzz number')
else: print('This is not a buzz number')
