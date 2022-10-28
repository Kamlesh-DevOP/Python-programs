h=int(input('Enter hours'))
d=h//24
hours=h%24
day=d%7
week=d//7

print('Days:',day, '\nHours:',hours, '\nWeeks', week)