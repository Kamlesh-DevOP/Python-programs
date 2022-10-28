a1=0
a2=0
a3=0
a4=0
for _ in range(10):
    age=int(input('Enter your age: '))
    if 18<=age<28:
        a1+=1
    if 28<=age<38:
        a2+=1
    if 38<=age<48:
        a3+=1
    if 48<=age<58:
        a4+=1
    
print(a1,'Members are in age group of 18-28')
print(a2,'Members are in age group of 28-38')
print(a3,'Members are in age group of 38-48')
print(a4,'Members are in age group of 48-58')


