'''
ab
cdef
ghijkl
mnopqrst'''
n=int(input('Enter the number of terms: '))
a='a'
for i in range(1,n+1):
    for j in range(1,i*2+1):
        print(a,end='')
        a=chr(ord(a)+1)
    print()