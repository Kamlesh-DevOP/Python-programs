def words_with_max_vowels(filename):
    f=open(filename)
    wordlist=f.read().split()
    max=0
    l=[]
    for word in wordlist:
        vc=0
        for letter in word:
            if letter.lower() in 'aeiou':
                vc+=1
        if max<=vc:
            if max==vc:
                l.append(word)
            else:
                max=vc
                l.clear()
                l.append(word)
        
    return l

print(words_with_max_vowels('lorem ipsum.txt'))

#OMG no program ever has given me THIS MUCH SATISFACTION!!
#gowtham's face when i showed this to him after correcting the mistakes in his code >>>>>>>
#me==orz