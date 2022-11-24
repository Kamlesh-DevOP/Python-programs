num=int((input('Enter a number: ')))
if num==1 or num==0:
     print('Neither a prime nor composite')
     quit()
for i in range(2,num):
    if num%i==0:
        print('Composite number')
        break
else:
    print('It is a prime number')