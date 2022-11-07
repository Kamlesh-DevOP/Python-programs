#list with strings containing most number of vowels
#record question
l=eval(input('Enter list: '))
vowel=[]
for i in l:
    count=0
    for j in i:
        if j in 'AEIOUaeiou':
            count+=1
    vowel+=[count]
max_index=vowel[0]
for i in range(len(vowel)):
    if vowel[i]>max_index:
        max_index=i #getting index value of the element containing highest number of vowels
print(l[max_index], 'is the string with maximum vowels')
