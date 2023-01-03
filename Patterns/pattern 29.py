for i in range(65,71):
    for j in range(i,71):
        print(' ',end='')
    for k in range(i,64,-1):
        print(chr(k),end='')
    for l in range(66,i+1):
        print(chr(l),end='')
    print()
'''
     A  
    BAB
   CBABC
  DCBABCD
 EDCBABCDE
FEDCBABCDEF
'''