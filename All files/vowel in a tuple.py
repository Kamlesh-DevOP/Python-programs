#count and display the vowels in tuples of strings
t=()
n=int(input('Enter n: '))
for i in range(n):
    t+=(input('Enter string: '),)
print(t)
for word in t:
    count=0
    for letter in word:
        if letter.lower() in 'aeiou':
            count+=1
    print(count,end=' ')