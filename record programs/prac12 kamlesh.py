with open('data.txt','w') as f:
    n=int(input('Enter number of lines: '))
    s=''
    for i in range(n):
        s=s+input('Enter a line: ')+'\n'
    f.write(s)
    print(s)
    print('File created successfully')
print('''MENU
1. Count the number of words
2. Display Palindrome words
3. Display words starting and ending with a vowel
4. Exit''')
while True:
    ch=int(input('Enter option: '))
    if ch==1:
        with open('data.txt','r') as f:
            print('Number of words:',len(f.read().split()))
    elif ch==2:
        flag=0
        with open('data.txt','r') as f:
            for i in f.read().split():
                if i==i[::-1]:
                    print(i,end=' ')
                    flag=1
        if flag==0:print('No palindromes')
    elif ch==3:
        flag=0
        with open('data.txt','r') as f:
            for i in f.read().split():
                m=i.lower()
                if m[0] in 'aeiou' and m[-1] in 'aeiou':
                    print(i, end=' ')
                    flag=1
        if flag==0: print('No such words')
    elif ch==4:
        print('Exiting...')
        break
    else: print('Invalid option')