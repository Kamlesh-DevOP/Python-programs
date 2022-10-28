ll=int(input('enter lower limit: '))
ul=int(input('enter upper limit: '))
a=-1
b=1
for i in range(ul):
    c = a + b
    a = b
    b = c
    if c>ll and c<ul:
        print(c)