n1=input('Enter your name: ')
n2=input('Enter your crush\'s name: ')
count=0
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
    