'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string &quot;&quot;.

Example 1:
Input: strs = ['flower','flow','flight']
Output: ''
Example 2:
Input: strs = ['dog','racecar','car']
Output: ''
Explanation: There is no common prefix among the input strings.
'''
arr=eval(input('Enter array of strings: '))
minelement=arr[0]

b=True
if len(arr)==1:
    print(arr[0])
for word in arr:
    if len(word)<len(minelement):
        minelement=word
arr.remove(minelement)

for i in arr:
    if i==minelement:
        print(minelement)
        break
    else:
        break

minelementlength=len(minelement)
for i in range(1,minelementlength+2):
    for word in arr:
        check=minelement
        if word[0:i]!=check[0:i]:
            print(minelement[:i-1])
            b=False
            break
    if not b:
        break

#guha's question in class 11 annual practicals. thank god i didnt get this... literally went through a breakdown and 2 depressing days to finally 
#complete this
#its a leetcode easy problem btw
