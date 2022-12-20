'''
ABCDEDCBA
 ABCDCBA
  ABCBA
   ABA
    A
'''
for i in range(69,64,-1):
    for j in range(i+1,70):
        print(' ', end='')
    for k in range(65,i+1):
        a = chr(k)
        print(a,end='')
    for m in range(i-1,64,-1):
        b = chr(m)
        print(b, end='')
    print()