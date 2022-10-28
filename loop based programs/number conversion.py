print('''Choose: 
1.Decimal to Binary 
2. Binary to Decimal 
3. Octal to decimal 
4. Exit ''')
q=int(input('Enter the number: '))
if q==1:
    n=int(input('Enter decimal number: '))
    binary=''
    while n!=0:
        r=n%2
        a=str(r)
        n=n//2
        binary=a+binary
    print("The binary form of the number is",binary)

elif q==2:
    n=int(input('Enter binary number: '))
    s=0
    i=0
    while n!=0:
        r=n%10
        n=n//10
        dig=r*2**i
        s+=dig
        i+=1
    print(s)

elif q==3:
    n=int(input('Enter octal number: '))
    s=0
    i=0
    while n!=0:
        r=n%10
        n=n//10
        dig=r*8**i
        s+=dig
        i+=1
    print(s)