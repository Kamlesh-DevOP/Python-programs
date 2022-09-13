ch=input('Enter an alphabet: ')
if ch>='A' and ch<='Z':
    print('It is in UPPER CASE')
    print(ch.lower())
elif ch>='a' and ch<='z':
    print('It is in lower case')
    print(ch.upper())
else: 
    print('Invalid character')