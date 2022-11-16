#record question
t=()
n=int(input('Enter number of tuples: '))
m=int(input('Enter number of elements per tuple: '))
for i in range(n):
    t1=()
    for j in range(m):
        t1+=(int(input('Enter element: ')),)
    t+=(t1,)
print(t)
tmean=()
for k in t:
    sum=0
    for l in k:
        sum+=l
    mean=sum/m
    tmean+=mean,
summean=0
for mean1 in tmean:
    summean+=mean1
mean_of_means=summean/n
print('Tuple of means=',tmean,'\nMean of means',mean_of_means)