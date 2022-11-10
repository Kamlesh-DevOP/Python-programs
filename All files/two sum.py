#target is the sum of any two numbers, print the indices of the 2 numbers when added gives the target
target=int(input('Enter target: '))
nums=eval(input('Enter list: '))
for i in range(len(nums)):
    for j in range(len(nums)):
        if i==j:
            continue
        if nums[i]+nums[j]==target:
            print(i,j)
            break