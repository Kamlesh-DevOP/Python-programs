dividend=int(input('Enter dividend: '))
divisor=int(input('Enter divisor: '))
if dividend>divisor:
    pass
if dividend<divisor:
    divisor,dividend=dividend,divisor
while divisor!=0:
    rem=dividend%divisor
    dividend=divisor
    divisor=rem
print('GCD of these numbers is',dividend)

