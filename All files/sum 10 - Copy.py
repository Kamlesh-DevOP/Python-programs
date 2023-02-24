#Question 2
'''
2. Take an input string parameter and determine if exactly 3 question marks exist between every pair of numbers
that add up to 10. If so, return true, otherwise return false. Some examples test cases are below:
&quot;arrb6???4xxbl5???eee5&quot; =&gt; true
&quot;acc?7??sss?3rr1??????5&quot; =&gt; true
&quot;5??aaaaaaaaaaaaaaaaaaa?5?5&quot; =&gt; false
&quot;9???1???9???1???9&quot; =&gt; true
&quot;aa6?9&quot; =&gt; false
'''
#Code:
st=input('Enter string: ')
for i in range(len(st)-4): #a3???4????
    if st[i].isdigit() and st[i+4].isdigit():
        if int(st[i])+int(st[i+4])==10:
            if st[i+1]==st[i+2]==st[i+3]=='?':
                flag=True
                break
            else:
                flag=False
        else:
            flag=False
    else:
        flag=False
else:
    flag=False
if flag:
    print('True')
else:
    print('False')

#Outputs:
'''
Enter string: &quot;arrb6???4xxbl5???eee5&quot; =&gt;
True

Enter string: &quot;acc?7??sss?3rr1??????5&quot; =&gt;
False

Enter string: &quot;5??aaaaaaaaaaaaaaaaaaa?5?5&quot; =&gt;
False

Enter string: &quot;9???1???9???1???9&quot; =&gt;
True

Enter string: &quot;aa6?9&quot; =&gt;
False

Enter string: a@3???5???5
True
'''
#class 11 annual practical program 2