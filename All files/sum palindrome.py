str1=input('Enter a number: ')
str2=input('Enter another number: ')
num1=int(str1)
num2=int(str2)
res=num1+num2

str_res=str(res)
if len(str_res)==2:
    rev2dig=str_res[-1]+str_res[-2]
    if rev2dig==str_res:
        print('Your sum is a palindrome')
    else: print('Your number is not a palindrome')

if len(str_res)==3:
    rev3dig=str_res[-1]+str_res[-2]+str_res[-3]
    if rev3dig==str_res:
        print('Your sum is a palindrome')
    else: print('Your number is not a palindrome')

if len(str_res)==4:
    rev4dig=str_res[-1]+str_res[-2]+str_res[-3]+str_res[-4]
    if rev4dig==str_res:
        print('Your sum is a palindrome')
    else: print('Your number is not a palindrome')

