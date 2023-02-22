'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string &quot;&quot;.

Example 1:
Input: strs = [&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
Output: &quot;fl&quot;
Example 2:
Input: strs = [&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
Output: &quot;&quot;
Explanation: There is no common prefix among the input strings.
'''
arr=eval(input('Enter array of strings: '))
minelement=arr[0]
b=True
for word in arr:
    if len(word)<len(minelement):
        minelement=word
minelementlength=len(minelement)
arr.remove(minelement)

for i in range(1,minelementlength+1):
    for word in arr:
        check=minelement
        if word[0:i]!=check[0:i]:
               
            b=False
            break
    if not b:
        break
print(minelement[:i-1])

#guha's question in annual practicals. thank god i didnt get this... literally went through a breakdown and 2 depressing days to finally 
#complete this
#its a leetcode easy problem btw
