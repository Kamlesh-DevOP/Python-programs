'''
a
ab
abc
abcd'''
n=int(input('Enter the number of terms: '))
i=1
while i<=n:
    ch='a'
    j = 1
    while j<=i:
        print(ch,end=' ')
        ch=chr(ord(ch)+1)
        j+=1
    i+=1
    print()
