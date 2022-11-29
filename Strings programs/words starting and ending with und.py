string=input('Enter a word: ')
st=string.lower()
k=len(st)-6
ans=''
if st[:3]=='und' and st[-3:]=='und':
    ans+='und'
    ans+=('$'*k)
    ans+='und'
    print(ans)
else:
    print('Word not satisfied the condition')