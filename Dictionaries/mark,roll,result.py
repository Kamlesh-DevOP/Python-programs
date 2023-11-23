''' 
Create a dictionary “Student” , of ‘n’ students with the following
Rollno – integer- KEY
And values being:
Name – string
Stream – string
Marks – integer list of size 5
Result – string which is filled with “****”
Update Result field to “Pass” only if the student has pass marks(>=40)
in all subjects, “Fail” otherwise .Display the details of all Students
'''


d={}
n=int(input('n: '))
for i in range(n):
    roll=int(input('roll: '))
    name=input('name: ')
    stream=input('stream: ')
    mark=int(input('marks: '))
    result='****'
    if mark>=40:
        result='PASS'
    else:
        result='FAIL'
    d[roll]=(name,stream,mark,result)
    print(d)