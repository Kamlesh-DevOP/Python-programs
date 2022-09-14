'''
@@@@@A
@@@@B
@@@C
@@D
@E
'''
ch=65
for i in range(5,0,-1):
    print('@'*i,chr(ch),end='',sep='')
    ch+=1
    print()
