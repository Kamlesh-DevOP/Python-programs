print('1 for executing using slicing and 2 for without slicing')
q=int(input('With or without slicing? '))
if q==1:
    st=input('Enter a string: ')
    b=st[::-1]
    if b==st:
        print('Palindrome')
    else: print('Not a palindrome')

if q==2:
    str=input('Enter a string: ')
    b=''
    for i in range(-1,-len(str)-1,-1):
        b+=str[i]
    if str==b:
        print('Palindrome')
    else: print('Not a palindrome')