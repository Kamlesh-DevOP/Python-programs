#list with strings containing most number of vowels
#record question
l=eval(input('Enter list: '))
vowel=[]
for i in l:
    count=0
    for j in i:
        if j in 'AEIOUaeiou':
            count+=1
    vowel.append(count)
print(vowel)
max=vowel[0]
for i in vowel:
    if i>max:
        max=i
for j in range(len(vowel)):
    if vowel[j]==max:
        print(l[j])
        