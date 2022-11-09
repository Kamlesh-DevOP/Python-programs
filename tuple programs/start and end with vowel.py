#count and display the strings starting and ending with vowels in tuples of strings
t=()
n=int(input('Enter n: '))
for i in range(n):
    t+=(input('Enter string: '),)
print(t)
for word in t:
    if word[-1] and word[0] in 'AEIOUaeiou':
        print(word)