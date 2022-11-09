#leeEetcode -> leetcode
#if an alphabet is followed by the capital of the same letter, both to be removed
x=input('Enter string: ')
l=[]
str=''
for i in x:
    if len(l)==0:
        l.append(i)
    elif abs(ord(l[-1])-ord(i))==32:
        l.pop()
    else:
        l.append(i)
for k in l:
    str+=k
print(str)