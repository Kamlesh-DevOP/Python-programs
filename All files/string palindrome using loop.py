st=input('Enter a string: ')
mid=int(len(st)/2)
rev=-1
for a in range(mid):
    if st[a]==st[rev]:
        rev-=1
    else:
        print('Not a palindrome')
        break
else:
    print('Palindrome')
    #if we wanna do smth after the loop gets over, use for else like here