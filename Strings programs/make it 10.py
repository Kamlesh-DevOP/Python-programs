s = list(input())
while '01' in ''.join(s):
    l = ''.join(s).split('01')
    s = ''.join(l)
print(s)