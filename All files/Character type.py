char=str(input('Enter any character from your keyboard: '))
if char>='a' and char<='z' or char>='A' and char<='Z':
    print('Alphabet')
    if char>='a' and char<='z':
        print('lower case')
    else:
        print('UPPER CASE')
elif '0'<=char<='9':
    print('Number')
else:
    print('Invalid character')
    