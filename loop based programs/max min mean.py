n=int(input('Enter n: '))
num=int(input('Enter a number: '))
max=min=num
count,sum=1,num
for i in range(n-1):
    num=int(input('Enter a number: '))
    if num>=max:
        max=num
    elif num<min:
        min=num
    count+=1
    sum+=num
mean=sum/count
print('Maximum number is:',max,'\nMinimum number is: ',min,'\nMean number is: ',mean)