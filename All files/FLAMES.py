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
flames=list('FLAMES')
num=num%6
k=0
cou=0
length=len(flames)
while k<length:
    cou+=1
    if cou==num:
        del flames[cou-1]
    k+=1
    length-=1
#incomplete
















'''
l=[]
name=n1+n2
for i in name:
    if i in l:
        continue
    else:
        l.append(i)
for c in l:
    count+=1
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