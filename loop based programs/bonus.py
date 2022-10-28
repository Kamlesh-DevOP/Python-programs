sal=int(input('Enter your salary: '))
Sex=input('Enter your sex: ')
sex=Sex.lower()
if sex=='m':
    bonus=5*sal/100
    salary_bonus=sal+bonus
    print('Your bonus is ',salary_bonus)
    if sal<10000:
        total_sal=(2*sal/100)+salary_bonus
        print('Your salary for the month is', total_sal)
    else: print('Your salary for the month is', salary_bonus)
elif sex=='f':
    bonus=10*sal/100
    salary_bonus=sal+bonus
    print('Your bonus is ',salary_bonus)
    if sal<10000:
        total_sal=(2*sal/100)+salary_bonus
        print('Your salary for the month is', total_sal)
    else: print('Your salary for the month is', salary_bonus)
else: print('Invalid credentials')
