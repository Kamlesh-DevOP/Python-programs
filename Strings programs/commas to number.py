'''
Write a program that accepts a non-negative number should convert the number to a
string and add commas as a thousand separators. For example, if the number is 1000000
should display '1,000,000'
'''
num=input('Enter number: ')
l=list(num)
for i in range(len(num)-3,0,-3):
    l.insert(i,',')
for i in l:
    print(i,end='')
#class 11 annual practicals- Aadithya Iniyavan's program