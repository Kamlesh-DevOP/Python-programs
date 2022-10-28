num=int(input('Enter a 3 digit number: '))
last_2=num%100
first_digit=num//100

ones=last_2%10
tens=last_2//10
hundreds=first_digit
actual=hundreds,tens,ones
reverse= ones,tens,hundreds

if actual==reverse:
     print('No change. This is a palindrome', '\nCannot reverse this number!')
else:
    print('Reverse of your 3 digit number is: ', ones, tens, hundreds, sep='')







'''My first mind blowing creative extraordinary program written on my own. Question asked by Ajeetha. Credits: Girls school cs
paper mid term 1. Funfact: I turned into legend this day (on the day of legend release) by talking to her overcoming my fear!
I'm so contented today'''
