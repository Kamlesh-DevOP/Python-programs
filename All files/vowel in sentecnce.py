sent=input('Enter a sentence: ')
vowel=0
for word in sent.split():
    for i in word:
        if i in 'AEIOUaeiou':
            vowel+=1
print('Number of vowels: ',vowel)