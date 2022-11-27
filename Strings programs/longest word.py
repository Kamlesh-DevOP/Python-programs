#WAP to keep reading words till quit is entered & display the longest word that start and ends with a vowel
l=[]
while True:
    s=input('Enter string: ')
    l+=[s]
    if s=='quit':
        break
max=l[0]
for i in l:
    if i[0] in 'aeiou' and i[-1] in 'aeiou':
        if len(i)>len(max):
            max=i
print(max)