showa=''
while True:
    st=input('Enter a string: ')
    if st in 'ENDend':
        break
    elif st[0]==st[-1]:
        showa+=st+','
    else:
        print('Nope')
print(showa)
