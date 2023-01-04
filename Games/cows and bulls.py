import random
word=['able','acid','aged','also','area','ball','band','bank','base','bath','call','calm','came','camp','card','dark','data','date','dawn','days','earn','ease','east','easy','edge']
num=random.randrange(0, len(word))
pick=word[num]
q=1
chance=1
print('Welcome to Cows and bulls!')
print('You have 10 chances to find the word! Good luck!')
while True:
    while chance<=10:
        print()
        print('Chance: ',chance) 
        guess=input('Enter your guess word of length '+str(len(pick))+': ') #wow +c can be used to concatenate a variable str into input statement
        if guess.isdigit():
            print('Only alphabets are supported')
        if guess.isupper():
           guess=guess.lower()
        bull=0
        cow=0
        if len(guess)==4:
            chance+=1
            for letter in range(len(pick)):
                if pick[letter] in guess:
                    if guess[letter]==pick[letter]:
                        bull+=1
                    elif guess[letter]!=pick[letter]:
                        cow+=1
            print('cow ',cow)
            print('bull ',bull)
            if bull==len(pick):
                print('Congrats!!')
                break
        else:
            print('Input 4 letter word only')
    if chance==11:
        print()
        print('Oopsies! you lost the game')
        print('The word was',pick)
    print()
    x=input('Do you want to play again?')
    if x.lower()=='no' or 'n':
        break
    elif x.lower()=='yes' or 'y':
        pass
    else:
        print('Oops I didnt get you! Please type in yes or no')