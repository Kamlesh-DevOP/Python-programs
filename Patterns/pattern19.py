'''
E69
DE68
CDE67
BCDE66
ABCDE65
'''
a='E'
v=69
for k in range(1,6):
    m=a
    m=chr(ord(m)-(k-1))
    for i in range(k):
        print(m,end=' ')
        m=chr(ord(m)+1)
    print(v)
    v-=1