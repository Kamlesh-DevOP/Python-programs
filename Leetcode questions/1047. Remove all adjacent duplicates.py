#delete adjacent repeating elements
s=input('Enter string: ')
stack=[]
st=''
for i in range(len(s)):
    if len((stack))==0:
        stack.append(s[i])
    elif stack[-1]==s[i]:
        stack.pop()
    else:
        stack.append(s[i])
for j in stack:
    st+=j
print(st)