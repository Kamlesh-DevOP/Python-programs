def no_of_lines():
    with open('file.txt','r') as f:
        print(len(f.readlines()))
def copyU():
    s=''
    with open('file.txt','r') as f:
        for i in f.read().split():
            if 'u' in i.lower():
                s+=i+' '
    with open('U words.txt','w') as f:
        f.write(s)
    print(s)
def swapcase():
    with open('file.txt','r') as f:
        str=f.read()
        str=str.swapcase()
    with open('file.txt','w') as f:
        f.write(str)
    print(str)

with open('file.txt','w') as f:
    pass

while True:
    x=input('Enter a line: ')
    with open('file.txt','a') as f:
        f.write(x)
        f.write('\n')
    ch=input('Do you want to continue: ')
    if ch.lower()=='n':
        break
    elif ch.lower()=='y':
        pass
    else:
        print('Invalid choice')
   
print('''\tMENU
1. Display number of lines
2. Copy the words containing 'U' into another file and display the new file
3. Convert the case of the letters(lower to upper and vice versa) in the original text file and
display the contents
4. Exit''')
ch=0
while True:
    ch=int(input('Enter menu: '))
    if ch==1:
        no_of_lines()
    elif ch==2:
        print('New file created. File contents:')
        copyU()
    elif ch==3:
        print('New file created. File contents: ')
        swapcase()
    elif ch==4:
        print('Exiting...')
        break
    else:
        print('Invalid choice')