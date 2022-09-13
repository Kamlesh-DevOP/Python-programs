#Write a program to take an integer a as an input and check whether it ends with 4 or 8.

while True:
    a=int(input('Enter a number: '))
    if a%10==4 or a%10==8:
        print(a,'Ends with',a%10)
    elif a%10!=4 or a%10!=8:
        print(a,'does not end with 4 or 8')
        
    