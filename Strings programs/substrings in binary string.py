#find the number of substrings starting and ending with 1 in a string of binary numbers
s=input('Enter binary string: ')
count=0
for i in range(len(s)):
    if s[i]=='1':
        adder=s.count('1',i+1,len(s))
        count+=adder
print(count)