char=str(input('Enter any character from your keyboard: '))
if char>='a' and char<='z' or char>='A' and char<='Z':
    print('Alphabet')
    if char in 'aeiouAEIOU':
        print('Vowel')
    else: print('Consonant')
elif '0'<=char<='9':
    print('Number')
elif char in '\n' or char in '\t' or char in ' ':
    print('White space')
else: print('Special symbol')