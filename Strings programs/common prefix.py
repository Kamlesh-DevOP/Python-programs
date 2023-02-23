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