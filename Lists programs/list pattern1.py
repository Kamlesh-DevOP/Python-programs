#[a,bb,ccc...n]
l=[]
ch='a'
n=int(input('Enter n: '))
for i in range(1,n+1):
    l.append(ch*i)
    ch=chr(ord(ch)+1)
print(l)
