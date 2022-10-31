name1=input('Enter your name: ')
name2=input('Enter your crush\'s name: ')
lst1=list(name1)
lst2=list(name2)
len1=len(lst1)
len2=len(lst2)
i=0
while i<len1:
    j=0
    while j<len2:
        if lst1[i]==lst2[j]:
            del lst1[i]
            del lst2[j]
            i-=1
            len1-=1
            len2-=1
        j+=1
    i+=1
num=len(lst1+lst2)
flames=list('SFLAME') #using SFLAME because 6%6=0 and we wanna cancel S in that case. Shifting S to 0 index can solve the problem
flames1=list('FLAMES')
for k in range(6,0,-1):
    member=num
    member=num%k
    ans=flames.pop(member)
    if len(flames)>0:
        x=flames.pop(-1)
        flames=[x]+flames
print(ans)

#partially crt
'''
if count%6==1:
    print('Friends''\nWe are just friends!')
elif count%6==2:
    print('Love''\nAww.. Love!')
elif count%6==3:
    print('Affectionate''\nA caring affectionable friend!')
elif count%6==4:
    print('Marriage''\nWe\'d better move to the next big step!')
elif count%6==5:
    print('Enemies''\nErr... Enemies.. Everybody wants to be my enemy...')
else:
    print('Sister''\nSister bro are best couples! ಥ_ಥ')
#incomplete'''