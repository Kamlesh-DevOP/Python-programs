print('''Choose: 
1.Decimal to Binary 
2. Binary to Decimal 
3. Octal to decimal 
4. Exit ''')
q=int(input('Enter the code from the menu: '))
if q==1:
    n=int(input('Enter a decimal: '))
    a=0
    d=0
    while n!=0:
        a+=((n%2)*(10**d))
        n//=2
        d+=1
    print('Binary form is',a)

elif q==2:
    n=int(input('Enter binary number: '))
    s,i=0,0
    while n!=0:
        r=n%10
        n=n//10
        dig=r*2**i
        s+=dig
        i+=1
    print('Decimal number is',s)

elif q==3:
    n=int(input('Enter octal number: '))
    s,i=0,0
    while n!=0:
        r=n%10
        n=n//10
        dig=r*8**i
        s+=dig
        i+=1
    print('Decimal number is',s)