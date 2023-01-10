import random
x=random.randint(1,100)
print(x)
for j in range(10):
    print('Chance: ',j+1)
    guess=int(input('Enter guess: '))
    if guess==x:
        print('You win!') 
        break
    elif x>guess:
        if x-guess<=3:
            print('Too Close')
        else:
            print('Too Low')
    elif x<guess:
        if guess-x<=3:
            print('Too Close')
        else:
            print('Too High')
else:
    print('You lost, the number was',x)