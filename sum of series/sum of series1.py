#print value of x^n/n!
x=int(input('Enter the x: '))
n=int(input('Enter the n: '))
sum=0
for k in range(1,n+1):
    p=1 #used for squaring number. here x multiplies itself n times
    for j in range(1,k+1): #used for squaring number. here x multiplies itself n times
        p*=x #used for ssquaring number. here x multiplies itself n times
    
    q=1 #used for factorial.
    for j in range(1,k+1): #used for factorial.
        q*=j #used for factorial.
    sum+=p/q
print(sum)
#from Ajeetha