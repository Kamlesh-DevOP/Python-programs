'''
Write a program to solve a classic ancient Chinese puzzle:
We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many
chickens do we have?
'''
#my method
for a in range(35):
    for b in range(35):
        if a+b==35 and 2*a+4*b==94:
            print(a,b)

#jayash TOP G's method
l=94
h=35
b=(l-2*h)/2
a=2*h-l/2
print(a,b)
