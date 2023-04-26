f=open('covid.txt')
print(f.read(4))
f.seek(10)
print(f.tell())