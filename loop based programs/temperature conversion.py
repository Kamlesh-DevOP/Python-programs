Q=input('Do you want to convert celsius to farenheit(c2f) or farenheit to celsius(f2c): ')
q=Q.lower()
if q=='f2c':
    f=float(input('Enter temperature in Farenheit: '))
    cel=5*(f-32)/9
    print('Temperature in celsius is', round(cel,2))
elif q=='c2f':
    cel=float(input('Enter temperature in Celsius: '))
    f=cel*(9/5)+32
    print('Temperature in farenheit is', round(f,2))
