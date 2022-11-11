nums=int(input('Enter list: '))
for i in range(len(nums)):
    for j in nums[i+1:]:
        if nums[i]==j:
            nums.remove(j)
        else:
            break
print(nums)