f=open('file.txt','r+')
x=f.read().split()
a='-'.join(x)
f.write(a)
f.close()
f=open('file.txt','w')
f.write(a)
