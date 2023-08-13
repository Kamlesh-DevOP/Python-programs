from NUMBER import *
print('''MENU
1. Check for palindromic numbers from a tuple
2. Generate special numbers within the range entered by the user
3. Exit''')
while True:
    ch=int(input('Enter choice: '))
    if ch==1:
        tup=tuple()
        n=int(input('Enter number of elements for the tuple: '))
        for i in range(n):
            tup+=int(input('Enter number: ')),
        l=[]
        for i in tup:
            if PALINDROME(i)==1:
                l.append(i)
        if l==[]: print('No palindromes present')
        else:
            for i in l:
                print(i, end=' ')
            print('are the palindrome numbers present in the tuple', tup)
    elif ch==2:
        ll=int(input('Enter lower limit: '))
        ul=int(input('Enter upper limit: '))
        l=[]
        if ll<ul:
            for i in range(ll,ul):
                if SPECIAL(i)==1:
                    l.append(i)
        else:
            print('Enter valid limits')
        if l==[]:
            print('No special numbers exist in the range',ll,'-',ul )
        else: 
            for i in l:
                print(i, end=' ')
            print()
    elif ch==3:
        print('Exiting...')
        break
    else:
        print('Enter valid menu')