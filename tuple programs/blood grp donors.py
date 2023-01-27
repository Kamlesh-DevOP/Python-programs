'''Read a nested tuple of name and blood group of 'n' donors. Read a blood group and display names of all matching donors
(eg) if input was B=(('alpha',”A+”), (“beta”, “O+”), (“gamma”, “AB+”), (“omega”,”O+”))
If blood group entered  is  O+
Output should be :
    beta
		   omega
'''
n=int(input('How many entries? '))
outer_tuple=()
for _ in range(n):
    name=input('Enter name: ')
    blood=input('Enter blood group: ')
    inner_tup=(name,blood)
    outer_tuple+=((inner_tup),)
print(outer_tuple)
inp=input('Enter name to be searched: ')
for i in outer_tuple:
    if i[1]==inp:
        print(i[0])
