def allvowels(tup):
    flag=0
    print('Searching for words with all vowels')
    for i in tup:
        i=i.lower()
        if 'a' in i and 'e' in i and 'i' in i and 'o' in i and 'u' in i:
            print(i)
            flag=1
    if flag==0:
        print('No such words')

def bmi(nesttup):
    t=tuple()
    for tup in nesttup:
        bmi=tup[2]/(tup[1]**2)
        bmi=round(bmi,2)
        if bmi<18.5:
            result='underweight'
        elif bmi<=24.9:
            result='normal weight'
        else:
            result='overweight'
        print(tup[0],bmi,result)

print('''MENU
1. Find words with all vowels
2. Find BMI
3. Exit''')
while True:
    ch=int(input('Enter your choice: '))
    if ch==1:
        tup=tuple()
        n=int(input('Enter number of elements: '))
        for i in range(n):
            tup+=(input('Enter word: ')),
        allvowels(tup)
    elif ch==2:
        T=tuple()
        n=int(input('Enter number of entries: '))
        for i in range(n):
            t=tuple()
            t+=input('Enter name: '),
            t+=float(input('Enter height in metres: ')),
            t+=float(input('Enter weight in kg: ')),
            T+=t,
        bmi(T)
    elif ch==3:
        break
    else: print('INVALID CHOICE')
    print()