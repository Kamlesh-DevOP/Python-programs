s=input('Enter a string: ')
count=0
for i in range(len(s)):
    if (s[i]).lower()==chr(ord('a')+i):
        count+=1
print(count)