'''write a menu driven PYTHON program with menu items
1) 12 - hour mode
2) 24 - hour mode
3) Exit.
The program has to accept 2 times in hrs and minutes and a choice
( 1 or 2 or 3) and display the sum of these two times '''
h1=int(input("enter the hour"))
m1=int(input("enter the minute"))
h2=int(input("enter the hour"))
m2=int(input("enter the minute"))
sum=h1*3600+h2*3600+m1*60+m2*60
s=sum%60
sum//=60
m=sum%60
sum//=60
h=sum
print('''Time conversion
1) 12 – hour mode
2) 24 – hour mode
3) Exit''')
while True:
    ch=int(input("Enter your choice"))
    if ch==1:
        if h>=12:
            h-=12
            print(h,":",m,":",s,"PM")
        else:
            print(h,":",m,":",s,"AM")
    elif ch==2:
          print(h1+h2,":",m,":",s)
    elif ch==3:
          break