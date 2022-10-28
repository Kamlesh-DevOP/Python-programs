mark1=int(input('Enter your marks in Computer science: '))
mark2=int(input('Enter your marks in Physics: '))
mark3=int(input('Enter your marks in Chemistry: '))
mark4=int(input('Enter your marks in Maths: '))
mark5=int(input('Enter your marks in English: '))
total=mark1+mark2+mark3+mark4+mark5
avg=total/5
if avg>=75:
    result='Distinction'
elif avg<=60 and avg<75:
    result='First division'
elif avg<=50 and avg<60:
    result='Second division'
else: result='FAIL'
print('Total marks obtained: ',total,'\tAggregate: ',avg,'\tResult: ',result)
