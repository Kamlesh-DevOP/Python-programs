       return 'No prime numbers in the generated list'

print('''MENU:
1. Generate list of 5 random numbers
2. Print highest and second highest numbers from the generated list
3. Print the prime numbers from the generated list
4. Exit''')
while True:
    ch=int(input('Enter a menu code: '))
    if ch==1:
        ll=int(input('Enter lower limit: '))        
        ul=int(input('Enter upper limit: '))
        print(Generate(ll,ul))
    elif ch==2:
        print(Max_SecMax()[0],'is the highest',Max_SecMax()[1],'is the second highest')
    elif ch==3:
        print(Prime())
    elif ch==4:
        print(‘Exiting…’)
        break
    else:
        print('Invalid option')

OUTPUT:
MENU:
1. Generate list of 5 random numbers
2. Print highest and second highest numbers from the generated list
3. Print the prime numbers from the generated list
4. Exit
Enter a menu code: 1
Enter lower limit: 1
Enter upper limit: 10
[9, 3, 3, 2, 7]
Enter a menu code: 2
9 is the highest 7 is the second highest
Enter a menu code: 3
[3, 2, 7]
Enter a menu code: 5
Invalid option
Enter a menu code: 1
