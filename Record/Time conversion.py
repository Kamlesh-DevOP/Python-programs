'''Aim: To convert the give (input) seconds
to hours minutes and seconds'''
s=int(input("Enter the seconds: "))
h=s//3600
s=s%3600
m=s//60
s%=60
print('Hours=',h,'\nMinutes=',m,'\nSeconds=',s)
