'''
1a
1b2b
1c2c3c
'''
n=int(input('Enter the number of terms: '))
ch='a'
for i in range(1,n+1):
    for k in range(1,i+1):
        print(k,ch,end='',sep='')
    print() 
    ch=chr(ord(ch)+1)