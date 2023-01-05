for i in range(1,6):
    ascii=65
    for j in range(1,i+1):
        print(chr(ascii),end=" ")
        ascii+=2
    print("#",i,end=" ")
    print()
'''
A # 1 
A C # 2 
A C E # 3
A C E G # 4
A C E G I # 5
'''