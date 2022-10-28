#Input name and marks, give result, avg, total, grade, result

name=input('Enter your name:')
mark1=int(input('Enter your marks in Computer science: '))
mark2=int(input('Enter your marks in Physics: '))
mark3=int(input('Enter your marks in Chemistry: '))
mark4=int(input('Enter your marks in Maths: '))
mark5=int(input('Enter your marks in English: '))
total=mark1+mark2+mark3+mark4+mark5
avg=total/5
print('Your name is',name)
print('Your total is', total)
print('Your average is', avg)
if avg>=90:
    print('Grade:A')
elif avg>=75:
    print('Grade:B')
elif avg>=40:
    print('Grade:C')
else:
    print('Grade:Fail')
if mark1>=40 and mark2>=40 and mark3>=40 and mark4>=40 and mark5>=40:
    print('Result: PASS')
else:
    print('Result: FAIL')
