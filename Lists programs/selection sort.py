arr=eval(input('Enter list: '))

for i in range(len(arr)):
    minindex=i
    for j in range(i,len((arr))):
        if arr[minindex]>arr[j]:
            arr[j],arr[minindex]=arr[minindex],arr[j]
print(arr)