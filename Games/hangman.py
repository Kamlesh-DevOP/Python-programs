#hangman
l=['mango','apple','orange']
temp=list(l)
import random as r
ch=input('play? ')
while ch=='yes':
    if l!=[]:
        word=l[r.randrange(0,len(l))]
        l.remove(word)
    else:
        l=list(temp)
        continue
    print('Number of letters= ',len(word))
    a=['*' for k in range(len(word))]
    hang='HANGMAN'
    k=0;n=[]
    while k<7:
        guess=input('Enter letter: ')
        if  guess not in n:
            if  guess in word:
                for chr in range(len(word)):
                    if guess==word[chr]:
                        a[chr]=guess
            else:
                k+=1
            n+=[guess]
        else:
            print('you have already guessed this')
        [print(n, end='') for n in a]
        print(hang[:k].rjust(15))
        if '*' not in a:
            print('you won')
            break
    else:
        print('the word was',word)
    ch=input('play?')