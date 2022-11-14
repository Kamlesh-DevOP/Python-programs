t=()
while True:
    mark1=int(input('enter mark 1: '))
    mark2=int(input('enter mark 2: '))
    mark3=int(input('enter mark 3: '))
    q=input('Do you want to continue: ')
    t+=((mark1,mark2,mark3),)
    if q=='y':
        pass
    else:
        break
print(t)
for i in range(len(t)):
    s=0
    for j in range(3):
        s+=t[i][j]
    avg=s/3
    print(avg)