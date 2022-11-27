'''
1 2 3 4 5 4 3 2 1 
  1 2 3 4 3 2 1 
    1 2 3 2 1   
      1 2 1     
        1
'''
for i in range(5,0,-1):
    for j in range(5-i,0,-1):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(k,end=' ')
    for m in range(i-1,0,-1):
        print(m,end=' ')
    print()
