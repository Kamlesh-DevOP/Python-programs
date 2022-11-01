l=eval(input('Enter a list: '))
for i in range(5):
    for j in range(i+1):
        print(l[i][j],end=' ')
    print()

#or 
print('='*50)
for i in range(5):
    for j in range(5):
        if i>=j:
            print(l[i][j],end=' ')
    print()