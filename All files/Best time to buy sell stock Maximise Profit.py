'''Best time to buy and sell stock to Maximise Profit Leetcode - 121'''
prices=eval(input('enter list of stock values: '))
min_so_far=prices[0]
li=[]
profit=0
for i in range(len(prices)):
    if prices[i]<min_so_far:
        min_so_far=prices[i]
    if prices[i]>min_so_far:
        profit=prices[i]-min_so_far
    li+=[profit]
print(max(li))