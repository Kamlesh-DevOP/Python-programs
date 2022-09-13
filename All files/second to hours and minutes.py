'''Aim: To convert the give (input) seconds
to hours minutes and seconds'''
s=int(input("Enter the seconds"))
m=s//60
S=s%60
M=m%60
H=m//60
print('Hours=',H,'\nMinutes=',M,'\nSeconds=',round(S,2))
