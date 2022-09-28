#Quarterly question
show=''
while True:
    st=input('Enter a string: ')
    if st in 'ENDend':
        break
    elif st[0]==st[-1]:
        show+=st+','
    else:
        print('Nope')
print(show)
