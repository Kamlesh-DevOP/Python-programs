def selection_sort(arr):
  for i in range(len(arr)):
    minindex=i
    for j in range(i,len((arr))):
      if arr[minindex]>arr[j]:
        arr[j],arr[minindex]=arr[minindex],arr[j]
  return arr

lst=[]
n=int(input('How many elements: '))
for i in range(n):
  lst.append(int(input('Enter element: ')))
print(selection_sort(lst))