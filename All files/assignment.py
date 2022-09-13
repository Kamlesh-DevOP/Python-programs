'''. Write a python program to get the following output
1-----99
2-----98
3-----97
. .
. .
. .
98-----2
99-----1
'''

for i in range(1,100):
    k=(100-i)
    print(i,'-----',k)