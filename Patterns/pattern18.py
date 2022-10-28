'''Generate the following pattern using nested loops :
A65
AB66
ABC67
ABCD68
ABCDE69'''
ch="A"
num=65
for i in range(1,6):
    for k in range(i):
        char=chr(ord(ch)+k)
        num=ord(char)
        print(char,end='')
    print(num)
