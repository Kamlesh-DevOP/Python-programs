ch=66
for k in range(4,-1,-1): 
    for j in range(k,0,-1):
        print(' ',end='')
    
    for j in range(65,ch):
        print(chr(j),end='')
    for j in range(ch-2,64,-1):
        print(chr(j),end='')
    print()
    ch+=1
#ajee struggled lol